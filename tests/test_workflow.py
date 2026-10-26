"""Checks on the continuous-integration workflow and on the development requirements."""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "checks.yml"
REQUIREMENTS = ROOT / "requirements-dev.txt"
README = ROOT / "README.md"
# Import name -> name on PyPI, for the third-party modules the tests import.
DISTRIBUTIONS = {"pytest": "pytest", "yaml": "PyYAML", "openpyxl": "openpyxl"}
TOOLS = {"pytest", "black", "flake8"}


def load():
    data = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    # PyYAML reads the key `on` as the boolean True.
    data["on"] = data.pop(True, data.get("on"))
    return data


def steps():
    return load()["jobs"]["checks"]["steps"]


def commands():
    return [step["run"] for step in steps() if "run" in step]


def pinned():
    pins = {}
    for line in REQUIREMENTS.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            name, version = line.strip().split("==")
            pins[name.lower()] = version
    return pins


def test_workflow_is_valid_yaml_with_one_job():
    data = load()
    assert data["name"]
    assert list(data["jobs"]) == ["checks"]


def test_workflow_runs_on_push_and_pull_request():
    assert set(load()["on"]) == {"push", "pull_request"}


def test_workflow_never_uses_pull_request_target_or_secrets():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "pull_request_target" not in text
    assert "secrets." not in text


def test_workflow_has_read_only_permissions():
    assert load()["permissions"] == {"contents": "read"}
    assert "permissions" not in load()["jobs"]["checks"]


def test_workflow_runs_on_ubuntu_and_windows_with_python_3_13():
    job = load()["jobs"]["checks"]
    assert job["runs-on"] == "${{ matrix.os }}"
    assert job["strategy"]["matrix"]["os"] == ["ubuntu-latest", "windows-latest"]
    assert job["strategy"]["matrix"]["python-version"] == ["3.13"]
    assert job["strategy"]["fail-fast"] is False
    setup = [s for s in steps() if s.get("uses", "").startswith("actions/setup-python@")]
    assert len(setup) == 1
    assert setup[0]["with"]["python-version"] == "${{ matrix.python-version }}"


def test_workflow_actions_are_pinned_to_a_version():
    uses = [step["uses"] for step in steps() if "uses" in step]
    assert uses
    assert all(re.fullmatch(r"[\w./-]+@(v\d+(\.\d+)*|[0-9a-f]{40})", use) for use in uses), uses


def test_workflow_checks_out_without_keeping_credentials():
    checkout = [s for s in steps() if s.get("uses", "").startswith("actions/checkout@")]
    assert len(checkout) == 1
    assert checkout[0]["with"]["persist-credentials"] is False


def test_workflow_installs_the_pinned_requirements_then_runs_the_three_tools():
    run = commands()
    install = [i for i, c in enumerate(run) if "requirements-dev.txt" in c]
    assert len(install) == 1 and "pip install" in run[install[0]]
    order = [
        next(i for i, c in enumerate(run) if tool in c) for tool in ("black", "flake8", "pytest")
    ]
    assert order == sorted(order) and min(order) > install[0]
    assert any(c.strip() == "black --check ." for c in run)
    assert any(c.strip() == "flake8" for c in run)
    assert any(c.strip() == "pytest" for c in run)


def test_requirements_are_pinned():
    lines = [
        line
        for line in REQUIREMENTS.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    assert all(re.fullmatch(r"[A-Za-z0-9_.-]+==\d+(\.\d+)*", line.strip()) for line in lines), lines
    assert set(pinned()) >= {"pytest", "black", "flake8", "openpyxl", "pyyaml"}


def test_requirements_cover_what_the_tests_import():
    imported = set()
    for path in (ROOT / "tests").glob("*.py"):
        for name in re.findall(r"^(?:import|from) (\w+)", path.read_text(encoding="utf-8"), re.M):
            imported.add(name)
    local = {path.stem for path in (ROOT / "tests").glob("*.py")}
    third_party = imported - set(sys.stdlib_module_names) - local
    assert third_party == set(DISTRIBUTIONS)
    assert {name.lower() for name in DISTRIBUTIONS.values()} <= set(pinned())
    assert TOOLS <= set(pinned())


def test_readme_shows_the_workflow_badge_next_to_the_license_badge():
    lines = README.read_text(encoding="utf-8").splitlines()
    badge = next(i for i, line in enumerate(lines) if "actions/workflows/checks.yml" in line)
    license_badge = next(i for i, line in enumerate(lines) if "License: CC BY-NC-SA" in line)
    assert abs(badge - license_badge) == 1
    assert lines[badge].startswith("  [![Checks](https://github.com/")
    assert "/actions/workflows/checks.yml/badge.svg)](https://github.com/" in lines[badge]
