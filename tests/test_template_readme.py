"""Checks on Template/README.md and on how the main README points to the templates."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "Template"
README = TEMPLATE / "README.md"
MAIN = ROOT / "README.md"
FOLDERS = ["Manufacturer", "Materials", "FileOpenSave"]


def read(path):
    return path.read_bytes().decode("utf-8")


def test_template_holds_exactly_the_three_folders_and_the_readme():
    assert sorted(p.name for p in TEMPLATE.iterdir()) == sorted([*FOLDERS, "README.md"])


def test_readme_has_one_row_per_folder():
    rows = [line for line in read(README).splitlines() if line.startswith("| [`")]
    assert [re.match(r"\| \[`(\w+)/`\]", row).group(1) for row in rows] == FOLDERS
    for folder, row in zip(FOLDERS, rows):
        assert f"]({folder})" in row


@pytest.mark.parametrize("folder", ["Materials", "FileOpenSave"])
def test_readme_links_to_the_readme_of_the_folder(folder):
    assert f"]({folder}/README.md)" in read(README)
    assert (TEMPLATE / folder / "README.md").is_file()


def test_readme_links_to_the_core_library_guide_and_lib_core():
    text = read(README)
    assert "](../docs/core-library.md)" in text
    assert "](../lib/core)" in text
    assert (ROOT / "docs" / "core-library.md").is_file()


def test_readme_gives_the_number_of_families_of_the_manufacturer_template():
    assert "25 core families" in read(README)


def test_main_readme_links_to_the_template_readme_and_its_folders():
    text = read(MAIN)
    assert "[README](Template/README.md)" in text
    for folder in FOLDERS:
        assert f"](Template/{folder})" in text


def test_main_readme_does_not_promise_empty_manufacturer_files():
    assert "Empty `geometry.py` and `material.py`" not in read(MAIN)
