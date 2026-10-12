# AI Test Automation Agent Lab

A practical Python-based engineering lab for building
reliable AI-assisted test automation agents.

## Objective

Demonstrate agent orchestration, safe tool invocation,
test execution, evidence collection, and evaluation.

## Planned technology stack

- Python
- LangGraph
- Model Context Protocol (MCP)
- Playwright
- Pytest
- LLM provider abstraction
- Evaluation harness
- Security guardrails

## Development methodology

The project follows phases and checkpoints.

Each checkpoint must satisfy its acceptance criteria
before the next checkpoint begins.

## Current status

Phase 0: Foundation

CP-0.1: Repository Foundation — Completed
CP-0.2: Deterministic CLI — Completed

## Local development

Requirements: Python 3.11+ and Git.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m ruff check .
```

## Security principles

- Explicitly allowed test targets only
- Human approval for high-risk actions
- No production credentials in the repository
- Evidence-based test reporting
- Deterministic evaluation where possible

## Architecture

Planned modules:

- agents: workflow orchestration
- llm: model provider abstraction
- mcp_tools: approved test tools
- guardrails: policy enforcement
- evaluation: agent quality assessment
- reporting: evidence and reports

## License

MIT


## Deterministic CLI (CP-0.2)

The project provides a minimal command-line interface
for deterministic test task planning.

### Run the CLI

```powershell
agent-lab run --task "Verify login validation"
```

Expected output:

```json
{
  "task": "Verify login validation",
  "status": "planned",
  "mode": "deterministic",
  "approved": false,
  "execution": "not_started"
}
```

### Current capabilities

- Accept a test task from the command line
- Normalize leading and trailing whitespace
- Reject empty tasks
- Produce deterministic JSON output
- Default to unapproved execution
- Never execute a real test in this baseline

### Verification

```powershell
python -m pytest -v
python -m ruff check .
```

### Limitations

This checkpoint does not implement LLM reasoning,
LangGraph orchestration, MCP tool integration,
or Playwright execution.

These features are planned for subsequent phases.