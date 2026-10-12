from pathlib import Path

import agent_lab


def test_package_is_importable():
    assert agent_lab is not None


def test_project_configuration_exists():
    project_root = Path(__file__).resolve().parents[2]

    assert (project_root / "pyproject.toml").is_file()
    assert (project_root / "README.md").is_file()
    assert (project_root / "LICENSE").is_file()
