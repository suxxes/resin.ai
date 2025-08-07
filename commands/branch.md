# Create New Branch

Create a new branch from main that follows the required naming pattern and switch to it.

## Features:
- Verifies the current branch is main
- Pulls latest changes from main
- Creates and switches to a new branch with correct naming pattern
- Validates branch name against required regex
- Offers guidance for correcting invalid branch names

## Usage:
- `/branch` - Interactive branch creation with validation
- `/branch feature XYZ-1234 My new feature` - Direct branch creation

## Branch Types:
- feature: New features or enhancements
- bugfix: Bug fixes
- chore: Maintenance, tooling, or configuration tasks
- release: Release preparation
- tests: Test additions or improvements

## Naming Pattern:
`^(feature|bugfix|chore|release|tests)\/[A-Za-z0-9]+-[0-9]+-[a-z0-9-]+$`

Which means:
1. Branch type (lowercase): feature, bugfix, chore, release, or tests
2. Jira board name (uppercase): e.g., XYZ, PRJ
3. Jira ticket number: e.g., 1234
4. Feature description converted to lower-kebab-case: e.g., My new feature -> my-new-feature

Example: `feature/XYZ-1234-my-new-feature`

## Process:
1. Verify current branch is main (`git branch --show-current`)
2. Update main branch (`git pull origin main`)
3. Collect branch information (type, Jira board, ticket number, description)
4. Format branch name according to pattern
5. Validate branch name against regex
6. Create and checkout new branch (`git checkout -b branch-name`)
7. Confirm successful branch creation

## Best Practices:
- Always branch from up-to-date main
- Use descriptive, concise feature descriptions
- Reference the correct Jira ticket
- Keep branch names all lowercase except for Jira board name
- Use hyphens (not underscores or spaces) in feature descriptions
- Keep branch names reasonably short

## Error Handling:
- If not on main, suggest checking out main first
- If branch name validation fails, explain the required format
- If branch contains file changes that disallow switching or updating branch, explain the reason
- Provide command to rename branch if needed: `git branch -m <newname>`
