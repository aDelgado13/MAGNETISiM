"""Checks on lib/core: headers, comments, loading, the family contract and the values."""

import ast
import importlib.util
import io
import json
import re
import subprocess
import sys
import tokenize
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "lib" / "core"
FIXTURE = ROOT / "tests" / "fixtures" / "lib_core_values.json"
MANUFACTURERS = [
    "AirCore",
    "CustomCore",
    "Ferroxcube",
    "IPT",
    "MagInc",
    "Micrometals",
    "TDK",
]
KINDS = ["geometry", "material"]
FILES = [(man, kind) for man in MANUFACTURERS for kind in KINDS]
FILE_IDS = [f"{man}/{kind}" for man, kind in FILES]

ART = r"""# ====================================================================#
# ====================================================================#
# ===   __  __    _    ____ _   _ _____ _____ ___ ____  _ __  __   ===#
# ===  |  \/  |  / \  / ___| \ | | ____|_   _|_ _/ ___|(_)  \/  |  ===#
# ===  | |\/| | / _ \| |  _|  \| |  _|   | |  | |\___ \| | |\/| |  ===#
# ===  | |  | |/ ___ \ |_| | |\  | |___  | |  | | ___) | | |  | |  ===#
# ===  |_|  |_/_/   \_\____|_| \_|_____| |_| |___|____/|_|_|  |_|  ===#
# ===                                                              ===#
# ====================================================================#
# ====================================================================#""".splitlines()
RULE = "# ====================================================================#"
BAR = "# " + "=" * 78
COPYRIGHT = [
    "# MAGNETISiM",
    "# Copyright (c) 2026 Universidad Politécnica de Madrid (UPM).",
    "# Licensed under CC BY-NC-SA 4.0 (see LICENSE). Free for non-commercial use;",
    "# the MAGNETISiM application itself is distributed under its own EULA.",
    "#",
]
AUTHORS = "# === AUTHORS    : Alberto Delgado, Alberto Vital                  ===#"
CONTACT = "# === CONTACT    : a.delgado@upm.es / www.magnetisim.com           ===#"
SECTION_RULE = re.compile(r"^# ={6,}$")
SECTION_TITLE = re.compile(r"^# ===\s+\S.* ={3,}$")
ALLOWED_NON_ASCII = set("é²³·")
CORE_TYPES = [("XY", "RZ"), ("1LEG", "2LEG", "3LEG"), ("SET", "WITH_I")]


def source(man, kind):
    return (CORE / man / f"{kind}.py").read_bytes().decode("utf-8").replace("\r\n", "\n")


def load_path(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def load_module(man, kind):
    return load_path(CORE / man / f"{kind}.py", f"lib_core_test_{man}_{kind}")


def family_functions(module):
    return {
        name[: -len("Geometry")]: fn
        for name, fn in vars(module).items()
        if name.endswith("Geometry") and callable(fn)
    }


def header_end(lines):
    """Index of the line that closes the copyright block (the second 78-character bar)."""
    bars = [i for i, line in enumerate(lines) if line == BAR]
    assert len(bars) >= 2
    return bars[1]


# --- the files ---------------------------------------------------------------


def test_lib_core_holds_exactly_the_14_files_and_the_readme():
    tracked = subprocess.run(
        ["git", "ls-files", "lib/core"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    expected = [f"lib/core/{man}/{kind}.py" for man, kind in FILES] + ["lib/core/README.md"]
    assert sorted(tracked) == sorted(expected)
    found = sorted(p.relative_to(ROOT).as_posix() for p in CORE.rglob("*.py"))
    assert found == sorted(t for t in tracked if t.endswith(".py"))


# --- header ------------------------------------------------------------------


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_header_is_exact(man, kind):
    lines = source(man, kind).split("\n")
    assert lines[:10] == ART
    assert lines[10] == f"# === FILE       : {kind}".ljust(len(RULE) - 4) + "===#"
    assert lines[11] == AUTHORS
    assert lines[12] == CONTACT
    description = f"{man} core {'geometries' if kind == 'geometry' else 'materials'}"
    assert lines[13] == f"# === DESCRIPTION: {description}".ljust(len(RULE) - 4) + "===#"
    assert lines[14:17] == [RULE, RULE, ""]
    assert lines[17] == BAR
    assert lines[18:23] == COPYRIGHT
    assert lines[23].startswith("# NOTE: ")
    end = header_end(lines)
    assert end > 23
    assert all(line.startswith("#") for line in lines[17 : end + 1])
    assert lines[end + 1] == ""
    assert all(len(line) <= 80 for line in lines[17:end] if "http" not in line)


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_header_has_no_internal_text(man, kind):
    text = source(man, kind)
    for forbidden in ("CREATED", "UPDATED", "All rights reserved", "prohibited", "Developed by"):
        assert forbidden not in text


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_note_gives_units_and_origin(man, kind):
    lines = source(man, kind).split("\n")
    note = " ".join(line.lstrip("# ") for line in lines[23 : header_end(lines)])
    assert "mm" in note if kind == "geometry" else "kW/m³" in note
    if (man, kind) in {
        ("TDK", "geometry"),
        ("Ferroxcube", "geometry"),
        ("MagInc", "geometry"),
        ("Micrometals", "geometry"),
    }:
        assert "dimension convention" in note and "Mass in g" in note
    if kind == "material" and man in {"TDK", "Ferroxcube", "MagInc", "Micrometals"}:
        assert "fitted by the MAGNETISiM team" in note


# --- comments, docstrings, text -------------------------------------------------


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_only_section_separators_remain_outside_the_header(man, kind):
    text = source(man, kind)
    lines = text.split("\n")
    end = header_end(lines)
    offenders = []
    for token in tokenize.generate_tokens(io.StringIO(text).readline):
        if token.type != tokenize.COMMENT or token.start[0] - 1 <= end:
            continue
        before = lines[token.start[0] - 1][: token.start[1]]
        if before.strip() or not (
            SECTION_RULE.match(token.string) or SECTION_TITLE.match(token.string)
        ):
            offenders.append((token.start[0], token.string))
    assert offenders == []


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_no_docstrings(man, kind):
    tree = ast.parse(source(man, kind))
    docstrings = [
        getattr(node, "name", "<module>")
        for node in ast.walk(tree)
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef))
        and ast.get_docstring(node, clean=False) is not None
    ]
    assert docstrings == []


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_only_allowed_non_ascii_characters(man, kind):
    text = source(man, kind)
    assert {c for c in text if ord(c) > 127} <= ALLOWED_NON_ASCII


@pytest.mark.parametrize("man,kind", FILES, ids=FILE_IDS)
def test_no_runs_of_blank_lines_or_trailing_spaces(man, kind):
    text = source(man, kind)
    assert "\n\n\n\n" not in text
    assert [n for n, l in enumerate(text.split("\n"), 1) if l != l.rstrip()] == []
    assert text.endswith("\n") and not text.endswith("\n\n")


# --- loading and the family contract -------------------------------------------


def assert_family_follows_contract(family, fn):
    references = fn(None, False)
    assert isinstance(references, tuple) and references, family
    first = fn(references[0], False)
    keys = tuple(first)
    assert keys[-3:] == ("Ae", "Ve", "Mass"), family
    assert fn("GeoParam", False) == keys[:-3], family
    for reference in references:
        assert tuple(fn(reference, False))[-3:] == ("Ae", "Ve", "Mass"), (family, reference)
    kind = fn(references[0], True)
    assert isinstance(kind, tuple) and len(kind) == 3, family
    assert all(value in group for value, group in zip(kind, CORE_TYPES)), (family, kind)
    assert fn(None, True) == kind


@pytest.mark.parametrize("man", MANUFACTURERS)
def test_geometry_families_follow_the_contract(man):
    families = family_functions(load_module(man, "geometry"))
    assert families
    for family, fn in families.items():
        assert_family_follows_contract(family, fn)


@pytest.mark.parametrize("man", MANUFACTURERS)
def test_materials_list_and_load(man):
    material = load_module(man, "material").Material
    names = material(None)
    assert isinstance(names, tuple) and names
    for name in names:
        values = material(name)
        assert values["Material"] == name
        assert {"muR", "Cond", "Phi", "Bmax", "Steinmetz", "DebyeParameter"} <= set(values)


def test_the_library_has_29_families_with_eer_instead_of_er():
    families = set()
    for man in MANUFACTURERS:
        families |= set(family_functions(load_module(man, "geometry")))
    assert len(families) == 29
    assert "EER" in families and "ER" not in families


# --- values --------------------------------------------------------------------


def encode(value):
    if isinstance(value, tuple):
        return {"__tuple__": [encode(v) for v in value]}
    if isinstance(value, list):
        return [encode(v) for v in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def measure(man):
    geometry = load_module(man, "geometry")
    result = {"geometry": {}, "material": {}}
    for family, fn in family_functions(geometry).items():
        references = fn(None, False)
        result["geometry"][family] = {
            "none": encode(references),
            "geoparam": encode(fn("GeoParam", False)),
            "type_none": encode(fn(None, True)),
            "type_ref": encode(fn(references[0], True)),
            "missing": encode(fn("__missing__", False)),
            "refs": {r: encode(fn(r, False)) for r in references},
        }
    material = load_module(man, "material").Material
    names = material(None)
    result["material"] = {
        "none": encode(names),
        "missing": encode(material("__missing__")),
        "items": {n: encode(material(n)) for n in names},
    }
    return result


def test_the_fixture_covers_the_expected_library():
    expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert list(expected) == MANUFACTURERS
    assert sum(len(f["refs"]) for m in expected.values() for f in m["geometry"].values()) == 664
    assert sum(len(m["material"]["items"]) for m in expected.values()) == 175


def test_readme_counts_match_the_library():
    expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
    families = {f for m in expected.values() for f in m["geometry"]}
    references = sum(len(f["refs"]) for m in expected.values() for f in m["geometry"].values())
    materials = sum(len(m["material"]["items"]) for m in expected.values())
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert (
        f"in {len(expected)} manufacturer folders ({', '.join(MANUFACTURERS)}): "
        f"{len(families)} core families, {references} core references and {materials} materials"
    ) in readme
    for part in ("CC BY-NC-SA 4.0 |", "PolyForm Noncommercial 1.0.0 |"):
        assert part in readme


@pytest.mark.parametrize("man", MANUFACTURERS)
def test_values_match_the_2_1_library(man):
    expected = json.loads(FIXTURE.read_text(encoding="utf-8"))[man]
    actual = measure(man)
    assert list(actual["geometry"]) == list(expected["geometry"])
    for family, values in expected["geometry"].items():
        assert actual["geometry"][family] == values, family
    assert actual["material"] == expected["material"]
    # Same text means the same floats and the same int/float types, not just ==.
    assert json.dumps(actual) == json.dumps(expected)
