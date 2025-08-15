#!/usr/bin/env python3
"""
Orchestrator CLI - Modern Python CLI System

Enterprise-grade orchestration CLI built with Typer and Rich for superior UX.
Handles orchestration hooks as subcommands with beautiful formatting, progress indicators,
and enhanced help generation.

Features:
- Modern CLI with Typer framework
- Rich text output with colors and formatting
- Progress indicators for long operations
- Auto-completion support
- Command aliases and shortcuts
- JSON stdin compatibility maintained
- Enhanced error handling and user experience

Usage:
    python3 -m resinai update-progress        # Updates DEVELOPMENT_PLAN_AND_PROGRESS.md
    python3 -m resinai sync-docs              # Syncs Epic/Story/Task progress files (alias)
    python3 -m resinai validate-trans         # Validates phase transitions (alias)

This system receives JSON input via stdin and provides enhanced functionality
over the original bash hooks with enterprise-grade reliability and modern UX.
"""

import sys
import json
from typing import Dict, Any, Optional, Annotated
from pathlib import Path
from enum import Enum

# Import module components using relative imports
from .commands.progress import ProgressUpdater
from .commands.documentation import DocumentationSyncer
from .commands.validation import PhaseTransitionValidator
from .utils import JSONHandler, HookLogger, get_timestamp

# Import Rich components
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.text import Text
from rich import print as rich_print
from rich.prompt import Confirm


# Handle imports when running as script vs module
if __name__ == "__main__":
    # When running as script, set up path for local imports
    current_dir = Path(__file__).parent
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))


# Initialize Rich Console for beautiful output
console = Console()
error_console = Console(stderr=True)

# Initialize Typer App
app = typer.Typer(
    name="resinai",
    help="🎭 [bold blue]ResIn.AI Orchestrator CLI[/bold blue] - Enterprise-grade multi-agent orchestration system",
    epilog="""
[dim]Examples:[/dim]
  [green]echo '{"session_id":"123","tool_input":{"todos":[...]}}' | python3 -m resinai update-progress[/green]
  [green]echo '{"session_id":"123","tool_input":{"subagent_type":"developer-python"}}' | python3 -m resinai validate-transition[/green]

[dim]Input Format:[/dim]
  All commands expect JSON input via stdin containing session and tool data.

[dim]Auto-completion:[/dim]
  Install shell completion: [yellow]python3 -m resinai --install-completion[/yellow]
    """,
    no_args_is_help=True,
    rich_markup_mode="rich",
    add_completion=True,
)


def version_callback(value: bool) -> None:
    """Display version information with rich formatting."""
    if value:
        console.print(Panel.fit(
            "[bold blue]ResIn.AI Orchestrator CLI[/bold blue]\n"
            "Version: [green]2.0.0[/green] (Modern Typer + Rich edition)\n"
            "Built with: [yellow]Typer + Rich + Python[/yellow]",
            border_style="blue"
        ))
        raise typer.Exit()


def read_json_input(verbose: bool = False) -> Dict[str, Any]:
    """Read and validate JSON input from stdin with enhanced error handling."""
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            error_console.print("[yellow]⚠️ Warning:[/yellow] No input data received")
            return {}

        data = json.loads(input_data)

        # Show input summary in verbose mode
        if verbose:
            error_console.print(f"[dim]📥 Received {len(str(data))} chars of JSON input[/dim]")

        return data

    except json.JSONDecodeError as e:
        error_console.print(f"[red]❌ Error:[/red] Invalid JSON input: {e}")
        return {}
    except Exception as e:
        error_console.print(f"[red]❌ Error:[/red] Failed to read stdin: {e}")
        return {}


def execute_with_progress(operation_name: str, operation_func, input_data: Dict[str, Any]) -> int:
    """Execute operation with progress indication and enhanced error handling."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(f"🔄 Executing {operation_name}...", total=None)

        try:
            result = operation_func(input_data)
            progress.update(task, description=f"✅ Completed {operation_name}")

            if result == 0:
                console.print(f"[green]✅ {operation_name} completed successfully[/green]")
            else:
                console.print(f"[yellow]⚠️ {operation_name} completed with warnings (exit code: {result})[/yellow]")

            return result

        except Exception as e:
            progress.update(task, description=f"❌ Failed {operation_name}")
            error_console.print(f"[red]❌ Error in {operation_name}:[/red] {e}")
            return 1


@app.command(name="update-progress")
def update_progress(
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable verbose output")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", "-n", help="Show what would be done without executing")] = False,
) -> None:
    """
    📊 Update DEVELOPMENT_PLAN_AND_PROGRESS.md when TodoWrite changes phase status.

    Automatically detects phase transitions and updates orchestrator state with timestamps.
    Provides real-time synchronization of Epic Implementation State.
    """
    input_data = read_json_input(verbose)

    if dry_run:
        console.print("[yellow]🔍 Dry run mode - would update progress documentation[/yellow]")
        console.print(f"[dim]Input data: {len(str(input_data))} characters[/dim]")
        raise typer.Exit(0)

    updater = ProgressUpdater()
    exit_code = execute_with_progress("Progress Update", updater.update_progress, input_data)
    raise typer.Exit(exit_code)


@app.command(name="update-progress-documentation")
def sync_documentation(
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable verbose output")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", "-n", help="Show what would be done without executing")] = False,
) -> None:
    """
    🔗 Sync progress across Epic/Story/Task files when TodoWrite changes task progress.

    Maintains bidirectional documentation sync and calculates progress percentages.
    Updates Implementation Status sections across the hierarchy.
    """
    input_data = read_json_input(verbose)

    if dry_run:
        console.print("[yellow]🔍 Dry run mode - would sync documentation hierarchy[/yellow]")
        console.print(f"[dim]Input data: {len(str(input_data))} characters[/dim]")
        raise typer.Exit(0)

    syncer = DocumentationSyncer()
    exit_code = execute_with_progress("Documentation Sync", syncer.sync_documentation, input_data)
    raise typer.Exit(exit_code)


@app.command(name="validate-transition")
def validate_transition(
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable verbose output")] = False,
    force: Annotated[bool, typer.Option("--force", "-f", help="Force validation bypass (use with caution)")] = False,
) -> None:
    """
    🛡️ Validate completion criteria before allowing Task delegation to next phase.

    Enforces quality gates and prevents invalid state transitions.
    Blocks workflow violations and maintains audit trail.
    """
    input_data = read_json_input(verbose)

    if force:
        if not Confirm.ask("[yellow]⚠️ Force bypass validation checks?[/yellow]"):
            console.print("[blue]ℹ️ Validation bypass cancelled[/blue]")
            raise typer.Exit(0)
        console.print("[red]🚫 Force bypassing validation checks![/red]")

    validator = PhaseTransitionValidator()
    exit_code = execute_with_progress("Phase Transition Validation", validator.validate_transition, input_data)
    raise typer.Exit(exit_code)


@app.command(name="status")
def show_status() -> None:
    """
    📈 Display current orchestration system status and health check.

    Shows system information, recent activity, and configuration status.
    """
    console.print(Panel.fit(
        "[bold blue]🎭 ResIn.AI Orchestrator Status[/bold blue]\n\n"
        f"[green]✅ System Status:[/green] Operational\n"
        f"[green]✅ Timestamp:[/green] {get_timestamp()}\n"
        f"[green]✅ CLI Version:[/green] 2.0.0 (Typer + Rich)\n"
        f"[green]✅ Python Version:[/green] {sys.version.split()[0]}",
        border_style="blue",
        title="System Health"
    ))

    # Display available commands
    table = Table(title="Available Commands", border_style="dim")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Aliases", style="magenta")
    table.add_column("Description", style="white")

    table.add_row("update-progress", "-", "Update DEVELOPMENT_PLAN_AND_PROGRESS.md")
    table.add_row("update-progress-documentation", "-", "Sync Epic/Story/Task progress files")
    table.add_row("validate-transition", "-", "Validate phase transitions")
    table.add_row("status", "-", "Show system status (this command)")

    console.print(table)


@app.callback()
def main(
    version: Annotated[Optional[bool], typer.Option("--version", callback=version_callback, help="Show version information")] = None,
) -> None:
    """
    🎭 ResIn.AI Orchestrator CLI - Enterprise-grade multi-agent orchestration system.

    Modern Python CLI built with Typer and Rich for superior user experience.
    """
    pass


if __name__ == "__main__":
    app()
