"""Checks on the repository layout and its tooling configuration."""

import configparser
import subprocess
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    """Run a git command at the repository root and return its stdout."""
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True, encoding="utf-8"
    )
    return result.stdout


def check_attr(path, *attributes):
    """Return {attribute: value} for a (possibly non-existent) path.

    Patterns are matched case-sensitively, as on Linux and macOS, even on Windows.
    """
    values = {}
    output = git("-c", "core.ignorecase=false", "check-attr", *attributes, "--", path)
    for line in output.splitlines():
        _, attribute, value = line.split(": ")
        values[attribute] = value
    return values


def ls_files_eol():
    """Yield (index_eol, attributes, path) for every tracked file."""
    for line in git("ls-files", "--eol").splitlines():
        info, path = line.split("\t", 1)
        index_eol, _, attributes = info.split(maxsplit=2)
        yield index_eol.removeprefix("i/"), attributes.strip().removeprefix("attr/"), path


# --- .gitattributes ---------------------------------------------------------


def test_files_stored_with_crlf_are_not_renormalized():
    # "git add --renormalize ." rewrites every text file stored with CRLF unless it is -text.
    offenders = [
        path
        for index_eol, attributes, path in ls_files_eol()
        if index_eol in ("crlf", "mixed") and attributes != "-text"
    ]
    assert offenders == []


def test_files_marked_text_are_stored_with_lf():
    offenders = [
        path
        for index_eol, attributes, path in ls_files_eol()
        if attributes.startswith("text") and index_eol not in ("lf", "none", "")
    ]
    assert offenders == []


@pytest.mark.parametrize("path", ["new_module.py", "lib/core/NewMaker/geometry.py"])
def test_new_python_files_use_crlf(path):
    assert check_attr(path, "text", "eol") == {"text": "set", "eol": "crlf"}


@pytest.mark.parametrize(
    "path", ["NOTES.md", ".github/ISSUE_TEMPLATE/x.yml", "config.yaml", "data/x.json"]
)
def test_new_text_files_use_lf(path):
    assert check_attr(path, "text", "eol") == {"text": "set", "eol": "lf"}


@pytest.mark.parametrize("path", ["Template/Materials/new.xlsx", "figure.png", "FIGURE.PNG"])
def test_spreadsheets_and_images_are_binary(path):
    assert check_attr(path, "binary", "diff") == {"binary": "set", "diff": "unset"}


# --- Python tooling -----------------------------------------------------------


def test_black_and_pytest_configuration():
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert config["tool"]["black"]["line-length"] == 100
    assert config["tool"]["pytest"]["ini_options"]["testpaths"] == ["tests"]


def test_flake8_configuration():
    parser = configparser.ConfigParser()
    parser.read(ROOT / ".flake8", encoding="utf-8")
    flake8 = parser["flake8"]
    assert flake8.getint("max-line-length") == 100
    assert "E203" in flake8["extend-ignore"]
    excluded = {item.strip() for item in flake8["exclude"].replace("\n", ",").split(",")}
    assert {"lib/core", "Template"} <= excluded


@pytest.mark.parametrize(
    "path", ["__pycache__/x.pyc", "tests/__pycache__/x.pyc", ".pytest_cache/v", "a.pyc", ".venv/x"]
)
def test_python_artifacts_are_ignored(path):
    assert git("check-ignore", "--no-index", path).strip() == path


# --- Repository content ---------------------------------------------------------

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tif", ".tiff"}


def tracked_files():
    """Paths of the files in the working tree that Git tracks (or is about to)."""
    paths = git("ls-files", "--cached", "--others", "--exclude-standard").splitlines()
    return [path for path in paths if (ROOT / path).is_file()]


def test_no_images_in_template_materials():
    # Plots copied from manufacturer datasheets are not redistributed.
    images = [
        path
        for path in tracked_files()
        if path.startswith("Template/Materials/") and Path(path).suffix.lower() in IMAGE_SUFFIXES
    ]
    assert images == []
    assert not [
        p for p in (ROOT / "Template" / "Materials").iterdir() if p.suffix.lower() in IMAGE_SUFFIXES
    ]


def test_schemas_folder_is_gone():
    assert not (ROOT / "schemas").exists()
    assert not [path for path in tracked_files() if path.startswith("schemas/")]


def test_nothing_links_to_schemas():
    this_file = Path(__file__).resolve().relative_to(ROOT).as_posix()
    linking = []
    for path in tracked_files():
        if path == this_file or Path(path).suffix.lower() in IMAGE_SUFFIXES | {".xlsx"}:
            continue
        text = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
        if "schemas/" in text or "/schemas" in text:
            linking.append(path)
    assert linking == []
