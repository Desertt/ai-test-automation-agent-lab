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

CP-0.1: Repository Foundation — In Progress

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
