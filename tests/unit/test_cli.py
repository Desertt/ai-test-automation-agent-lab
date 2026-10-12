import pytest

from agent_lab.cli import create_plan


def test_create_plan_is_deterministic():
    first = create_plan("Verify login validation")
    second = create_plan("Verify login validation")

    assert first == second
    assert first["status"] == "planned"
    assert first["mode"] == "deterministic"


def test_plan_does_not_execute():
    result = create_plan("Verify login validation")

    assert result["approved"] is False
    assert result["execution"] == "not_started"


def test_task_is_trimmed():
    result = create_plan("  Verify login  ")

    assert result["task"] == "Verify login"


@pytest.mark.parametrize("task", ["", " ", "\n"])
def test_empty_task_is_rejected(task):
    with pytest.raises(ValueError, match="Task cannot be empty"):
        create_plan(task)