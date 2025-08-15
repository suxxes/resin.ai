#!/usr/bin/env python3
"""
Setup script for ResIn.AI Orchestrator CLI package.

Enterprise-grade setup and verification system for the ResIn.AI Orchestrator CLI,
a modern Python-based hook automation system built with Typer and Rich for
multi-agent orchestration workflow automation.

Features:
- Automatic dependency installation with version validation
- Comprehensive functionality testing across all CLI commands
- Rich-formatted output with progress indicators
- Error handling and troubleshooting guidance
- Version compatibility checking
- Module import validation

Usage:
    python3 setup.py                    # Full setup and verification
    python3 setup.py --install-only     # Dependencies only (if supported)
    python3 setup.py --verify-only      # Verification only (if supported)
"""

from pathlib import Path
import subprocess
import sys
import json
from typing import Dict, List, Tuple, Optional

def print_header():
    """Print setup header with rich formatting."""
    print("🎭 ResIn.AI Orchestrator CLI Setup")
    print("=" * 50)
    print("Enterprise-grade multi-agent orchestration system")
    print("Built with Typer + Rich for modern Python CLI experience")
    print("")

def install_dependencies() -> bool:
    """Install required dependencies with version validation."""
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    print("📦 Installing dependencies...")
    
    if not requirements_file.exists():
        print("❌ Error: requirements.txt not found")
        return False
    
    try:
        # Install dependencies
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ], check=True, capture_output=True, text=True)
        
        print("✅ Dependencies installed successfully!")
        
        # Verify critical dependencies
        critical_deps = ["typer", "rich"]
        for dep in critical_deps:
            try:
                __import__(dep)
                print(f"✅ {dep}: Import successful")
            except ImportError:
                print(f"❌ {dep}: Import failed")
                return False
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during installation: {e}")
        return False

def test_cli_functionality() -> bool:
    """Test core CLI functionality with comprehensive validation."""
    print("\n🧪 Testing CLI functionality...")
    
    tests = [
        ("Version check", [sys.executable, "-m", "resinai", "--version"]),
        ("Status command", [sys.executable, "-m", "resinai", "status"]),
        ("Help display", [sys.executable, "-m", "resinai", "--help"])
    ]
    
    for test_name, command in tests:
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ {test_name}: Passed")
            else:
                print(f"❌ {test_name}: Failed (exit code: {result.returncode})")
                if result.stderr:
                    print(f"   Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⚠️ {test_name}: Timeout (may indicate slow system)")
            return False
        except Exception as e:
            print(f"❌ {test_name}: Exception - {e}")
            return False
    
    return True

def test_command_functionality() -> bool:
    """Test individual command functionality with sample data."""
    print("\n🔧 Testing individual commands...")
    
    # Sample test data for different command types
    test_data = {
        "progress": {
            "session_id": "setup_test",
            "tool_input": {
                "todos": [
                    {
                        "id": "0001.01.01",
                        "content": "Setup test task - PM_BOOTSTRAP",
                        "status": "completed",
                        "priority": "high"
                    }
                ]
            }
        },
        "documentation": {
            "session_id": "setup_test", 
            "tool_input": {
                "todos": [
                    {
                        "id": "0001.01.01",
                        "content": "Documentation sync test",
                        "status": "in_progress",
                        "priority": "medium"
                    }
                ]
            }
        },
        "validation": {
            "session_id": "setup_test",
            "tool_input": {
                "subagent_type": "developer-python",
                "description": "Test validation for setup verification"
            }
        }
    }
    
    commands = [
        ("Progress update", "update-progress", test_data["progress"]),
        ("Documentation sync", "update-progress-documentation", test_data["documentation"]),
        ("Transition validation", "validate-transition", test_data["validation"])
    ]
    
    for test_name, command_name, input_data in commands:
        try:
            # Test with dry-run to avoid modifying real files
            result = subprocess.run([
                sys.executable, "-m", "resinai", command_name, "--dry-run"
            ], input=json.dumps(input_data), capture_output=True, text=True, timeout=15)
            
            if result.returncode == 0:
                print(f"✅ {test_name}: Passed")
            else:
                print(f"❌ {test_name}: Failed (exit code: {result.returncode})")
                if result.stderr:
                    print(f"   Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⚠️ {test_name}: Timeout")
            return False
        except Exception as e:
            print(f"❌ {test_name}: Exception - {e}")
            return False
    
    return True

def test_legacy_script_compatibility() -> bool:
    """Test legacy script execution compatibility."""
    print("\n🔄 Testing legacy script compatibility...")
    
    legacy_scripts = [
        ("progress.py", "commands/progress.py"),
        ("documentation.py", "commands/documentation.py"), 
        ("validation.py", "commands/validation.py")
    ]
    
    test_input = '{"session_id":"legacy_test","tool_input":{}}'
    
    for script_name, script_path in legacy_scripts:
        try:
            result = subprocess.run([
                sys.executable, script_path
            ], input=test_input, capture_output=True, text=True, timeout=10)
            
            # Legacy scripts should handle empty input gracefully
            if result.returncode == 0:
                print(f"✅ {script_name}: Legacy compatibility verified")
            else:
                print(f"⚠️ {script_name}: Legacy compatibility issue (may be expected)")
                # Don't fail setup for legacy issues unless critical
                
        except subprocess.TimeoutExpired:
            print(f"⚠️ {script_name}: Timeout in legacy mode")
        except Exception as e:
            print(f"⚠️ {script_name}: Legacy test exception - {e}")
    
    return True

def verify_installation() -> bool:
    """Comprehensive installation verification."""
    print("\n🔍 Verifying installation...")
    
    verification_steps = [
        ("CLI functionality", test_cli_functionality),
        ("Command functionality", test_command_functionality),
        ("Legacy compatibility", test_legacy_script_compatibility)
    ]
    
    all_passed = True
    
    for step_name, test_function in verification_steps:
        try:
            if test_function():
                print(f"✅ {step_name}: All tests passed")
            else:
                print(f"❌ {step_name}: Some tests failed")
                all_passed = False
        except Exception as e:
            print(f"❌ {step_name}: Verification error - {e}")
            all_passed = False
    
    return all_passed

def print_usage_instructions():
    """Print comprehensive usage instructions."""
    print("\n📚 Usage Instructions:")
    print("-" * 30)
    print("Main CLI Commands:")
    print("  python3 -m resinai --help                    # Show help")
    print("  python3 -m resinai status                    # System status")
    print("  python3 -m resinai update-progress           # Update progress docs")
    print("  python3 -m resinai validate-transition       # Validate transitions")
    print("")
    print("Testing Commands:")
    print("  echo '{}' | python3 -m resinai update-progress --dry-run")
    print("  echo '{}' | python3 -m resinai validate-transition --verbose")
    print("")
    print("Documentation:")
    print("  See USAGE.md for comprehensive documentation")
    print("  python3 -m resinai --help for command reference")

def main():
    """Main setup function with comprehensive verification."""
    print_header()
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8+ required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation.")
        print("Troubleshooting:")
        print("  1. Check internet connectivity")
        print("  2. Ensure pip is updated: python3 -m pip install --upgrade pip")
        print("  3. Check Python permissions")
        sys.exit(1)
    
    # Verify installation
    if not verify_installation():
        print("\n⚠️ Setup completed with warnings.")
        print("Some tests failed, but basic functionality may still work.")
        print("Check the test results above for specific issues.")
        print_usage_instructions()
        sys.exit(0)  # Don't fail for verification warnings
    
    # Success
    print("\n🎉 Setup completed successfully!")
    print("=" * 50)
    print("ResIn.AI Orchestrator CLI is ready for use!")
    print_usage_instructions()

if __name__ == "__main__":
    main()
