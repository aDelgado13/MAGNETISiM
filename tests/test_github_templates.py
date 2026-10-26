"""Checks on the GitHub issue forms and the pull request template."""

import ast
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
ISSUE_TEMPLATES = ROOT / ".github" / "ISSUE_TEMPLATE"
FORMS = ["bug_report.yml", "feature_request.yml", "core_data.yml"]
ELEMENT_TYPES = {"markdown", "input", "textarea", "dropdown", "checkboxes"}


def load(name):
    return yaml.safe_load((ISSUE_TEMPLATES / name).read_text(encoding="utf-8"))


def core_families():
    """Families defined in lib/core, read from the source of each geometry.py (never run)."""
    families = set()
    for path in sorted((ROOT / "lib" / "core").glob("*/geometry.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name.endswith("Geometry"):
                families.add(node.name.removesuffix("Geometry"))
    return families


def element(form, element_id):
    matches = [item for item in form["body"] if item.get("id") == element_id]
    assert len(matches) == 1, element_id
    return matches[0]


def test_the_issue_template_folder_holds_exactly_the_expected_files():
    assert sorted(p.name for p in ISSUE_TEMPLATES.iterdir()) == sorted(FORMS + ["config.yml"])


@pytest.mark.parametrize("name", FORMS)
def test_form_has_name_description_and_body(name):
    form = load(name)
    assert isinstance(form, dict)
    for key in ("name", "description"):
        assert isinstance(form[key], str) and form[key].strip()
    assert isinstance(form["body"], list) and form["body"]
    assert any(item["type"] != "markdown" for item in form["body"])


@pytest.mark.parametrize("name", FORMS)
def test_form_elements_are_well_formed(name):
    ids = []
    for item in load(name)["body"]:
        assert item["type"] in ELEMENT_TYPES
        assert "attributes" in item
        if item["type"] == "markdown":
            assert item["attributes"]["value"].strip()
            continue
        assert item["attributes"]["label"].strip()
        assert re.fullmatch(r"[A-Za-z0-9_-]+", item["id"])
        ids.append(item["id"])
        if item["type"] == "dropdown":
            options = item["attributes"]["options"]
            assert options and len(options) == len(set(options))
    assert len(ids) == len(set(ids)), "repeated id"


@pytest.mark.parametrize(
    "name, label", [("bug_report.yml", "bug"), ("feature_request.yml", "enhancement")]
)
def test_form_labels(name, label):
    assert load(name)["labels"] == [label]


def test_core_data_label():
    assert load("core_data.yml")["labels"] == ["core-data"]


def test_bug_report_asks_for_versions_and_steps():
    form = load("bug_report.yml")
    assert element(form, "magnetisim-version")["attributes"]["options"] == [
        "2.1.0",
        "2.0.0",
        "Other",
    ]
    for element_id in (
        "windows-version",
        "femm-version",
        "femm-setup",
        "steps",
        "expected",
        "actual",
        "attachments",
    ):
        element(form, element_id)


def test_feature_request_fields():
    form = load("feature_request.yml")
    for element_id in ("problem", "proposal", "alternatives"):
        element(form, element_id)


def test_core_data_fields():
    form = load("core_data.yml")
    assert element(form, "request-type")["attributes"]["options"] == [
        "New reference",
        "Correction",
        "New material",
    ]
    for element_id in ("manufacturer", "reference", "datasheet", "values", "what-is-wrong"):
        element(form, element_id)
    warnings = " ".join(i["attributes"]["value"] for i in form["body"] if i["type"] == "markdown")
    assert "image" in warnings.lower() and "link" in warnings.lower()


def test_lib_core_families_are_found():
    # Guard for the next test: the reader must see the families that exist today.
    assert {"E", "EI", "ETD", "PQ", "RM", "AIRXY", "IPTRZ"} <= core_families()


def test_family_dropdowns_match_lib_core():
    dropdowns = [
        item
        for name in FORMS
        for item in load(name)["body"]
        if item["type"] == "dropdown" and "famil" in item["attributes"]["label"].lower()
    ]
    assert dropdowns
    for dropdown in dropdowns:
        assert set(dropdown["attributes"]["options"]) == core_families()


def test_config_disables_blank_issues_and_links_the_website():
    config = load("config.yml")
    assert config["blank_issues_enabled"] is False
    assert [link["url"] for link in config["contact_links"]] == ["https://www.magnetisim.com"]
    for link in config["contact_links"]:
        assert link["name"].strip() and link["about"].strip()


def test_pull_request_template():
    text = (ROOT / ".github" / "pull_request_template.md").read_text(encoding="utf-8")
    assert (
        "- [ ] I have the right to submit this contribution and I license it as described in "
        "CONTRIBUTING.md (CC BY-NC-SA 4.0 for data and documentation, "
        "PolyForm Noncommercial 1.0.0 for code)" in text
    )
    assert "source" in text.lower()
