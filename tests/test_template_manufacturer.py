"""Checks on Template/Manufacturer: the template of a manufacturer for the user library."""

import ast
import copy
import io
import tokenize
from pathlib import Path

import pytest
from test_lib_core import (
    ALLOWED_NON_ASCII,
    ART,
    AUTHORS,
    BAR,
    CONTACT,
    COPYRIGHT,
    MANUFACTURERS,
    RULE,
    SECTION_RULE,
    SECTION_TITLE,
    assert_family_follows_contract,
    family_functions,
    header_end,
    load_module,
    load_path,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "Template" / "Manufacturer"
KINDS = ["geometry", "material"]
DESCRIPTIONS = {
    "geometry": "Template core geometries",
    "material": "Template core materials",
}
NOTES = {
    "geometry": [
        "# NOTE: Template for your own manufacturer. Copy geometry.py and material.py",
        "#       into core/<YourManufacturer>/ of your user library, rename the example",
        "#       references and replace their values with your datasheet values. Remove",
        "#       the families you do not need. Dimension letters and units: see",
        "#       docs/core-library.md.",
    ],
    "material": [
        "# NOTE: Template for the materials of your own manufacturer. Copy it with",
        "#       geometry.py into core/<YourManufacturer>/ of your user library, rename",
        "#       the example material and replace its values with the ones fitted from",
        "#       your datasheet curves. Parameters and units: see docs/core-library.md.",
    ],
}
EXAMPLE_MATERIAL = "Example-material"
CUSTOM_MATERIAL = "Ferrite"
OTHER_MANUFACTURERS = [man for man in MANUFACTURERS if man != "CustomCore"]


def source(kind):
    return (TEMPLATE / f"{kind}.py").read_bytes().decode("utf-8").replace("\r\n", "\n")


def load_template(kind):
    return load_path(TEMPLATE / f"{kind}.py", f"template_manufacturer_test_{kind}")


def template_families():
    return family_functions(load_template("geometry"))


def custom_families():
    return family_functions(load_module("CustomCore", "geometry"))


# --- the files and the header ---------------------------------------------------


def test_folder_holds_exactly_the_two_files():
    assert sorted(p.name for p in TEMPLATE.iterdir()) == ["geometry.py", "material.py"]


@pytest.mark.parametrize("kind", KINDS)
def test_header_is_exact(kind):
    lines = source(kind).split("\n")
    assert lines[:10] == ART
    assert lines[10] == f"# === FILE       : {kind}".ljust(len(RULE) - 4) + "===#"
    assert lines[11] == AUTHORS
    assert lines[12] == CONTACT
    assert lines[13] == f"# === DESCRIPTION: {DESCRIPTIONS[kind]}".ljust(len(RULE) - 4) + "===#"
    assert lines[14:17] == [RULE, RULE, ""]
    assert lines[17] == BAR
    assert lines[18:23] == COPYRIGHT
    end = header_end(lines)
    assert lines[23:end] == NOTES[kind]
    assert all(line.startswith("#") for line in lines[17 : end + 1])
    assert lines[end + 1] == ""
    assert all(len(line) <= 80 for line in lines[17:end])


@pytest.mark.parametrize("kind", KINDS)
def test_header_has_no_internal_text(kind):
    text = source(kind)
    for forbidden in ("CREATED", "UPDATED", "All rights reserved", "prohibited", "Developed by"):
        assert forbidden not in text


# --- comments, docstrings, text -------------------------------------------------


@pytest.mark.parametrize("kind", KINDS)
def test_only_section_separators_remain_outside_the_header(kind):
    text = source(kind)
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


@pytest.mark.parametrize("kind", KINDS)
def test_no_docstrings(kind):
    tree = ast.parse(source(kind))
    assert [
        getattr(node, "name", "<module>")
        for node in ast.walk(tree)
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef))
        and ast.get_docstring(node, clean=False) is not None
    ] == []


@pytest.mark.parametrize("kind", KINDS)
def test_only_allowed_non_ascii_characters(kind):
    text = source(kind)
    assert {c for c in text if ord(c) > 127} <= ALLOWED_NON_ASCII


@pytest.mark.parametrize("kind", KINDS)
def test_no_runs_of_blank_lines_or_trailing_spaces(kind):
    text = source(kind)
    assert "\n\n\n\n" not in text
    assert [n for n, line in enumerate(text.split("\n"), 1) if line != line.rstrip()] == []
    assert text.endswith("\n") and not text.endswith("\n\n")


# --- geometry: the families -----------------------------------------------------


def test_template_follows_the_contract_of_lib_core():
    families = template_families()
    assert families
    for family, fn in families.items():
        assert_family_follows_contract(family, fn)


def test_families_are_the_25_of_customcore():
    families = template_families()
    assert len(families) == 25
    assert list(families) == list(custom_families())


def test_families_are_not_those_of_air_or_ipt():
    names = set(template_families())
    assert not names & {"AIRXY", "AIRRZ", "IPTXY", "IPTRZ"}


def test_types_match_lib_core():
    custom = custom_families()
    for family, fn in template_families().items():
        assert fn(None, True) == custom[family](None, True), family
        for man in OTHER_MANUFACTURERS:
            other = family_functions(load_module(man, "geometry")).get(family)
            if other is not None:
                assert fn(None, True) == other(None, True), (man, family)


def test_each_family_has_one_example_reference():
    for family, fn in template_families().items():
        assert fn(None, False) == (f"{family}-example",), family


def test_example_values_are_the_first_reference_of_customcore():
    custom = custom_families()
    for family, fn in template_families().items():
        first = custom[family](None, False)[0]
        expected = custom[family](first, False)
        actual = fn(f"{family}-example", False)
        assert list(actual.items()) == list(expected.items()), family
        assert fn("GeoParam", False) == custom[family]("GeoParam", False), family


def test_unknown_reference_returns_base_return_as_in_lib_core():
    custom = load_module("CustomCore", "geometry")
    template = load_template("geometry")
    assert template.base_return == custom.base_return
    for family, fn in template_families().items():
        assert fn("__missing__", False) == custom.base_return, family


def _normalised(function, reference):
    node = copy.deepcopy(function)
    for statement in node.body:
        if isinstance(statement, ast.Assign) and statement.targets[0].id == "core_geometries":
            statement.value.keys = statement.value.keys[:1]
            statement.value.values = statement.value.values[:1]
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and child.value == reference:
            child.value = "<reference>"
    return ast.dump(node)


def test_code_pattern_is_the_one_of_lib_core():
    custom_tree = ast.parse(source_of_custom())
    template_tree = ast.parse(source("geometry"))
    custom_functions = {n.name: n for n in custom_tree.body if isinstance(n, ast.FunctionDef)}
    template_functions = {n.name: n for n in template_tree.body if isinstance(n, ast.FunctionDef)}
    assert list(template_functions) == list(custom_functions)
    custom = custom_families()
    for family in custom:
        name = f"{family}Geometry"
        first = custom[family](None, False)[0]
        assert _normalised(template_functions[name], f"{family}-example") == _normalised(
            custom_functions[name], first
        ), family


def source_of_custom():
    path = ROOT / "lib" / "core" / "CustomCore" / "geometry.py"
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


# --- material -------------------------------------------------------------------


def test_example_material_has_the_keys_of_a_lib_core_material():
    material = load_template("material").Material
    assert material(None) == (EXAMPLE_MATERIAL,)
    keys = tuple(material(EXAMPLE_MATERIAL))
    for man in MANUFACTURERS:
        library = load_module(man, "material").Material
        assert keys == tuple(library(library(None)[0])), man


def test_example_material_values_are_those_of_customcore():
    template = load_template("material")
    custom = load_module("CustomCore", "material")
    expected = custom.Material(CUSTOM_MATERIAL)
    actual = template.Material(EXAMPLE_MATERIAL)
    assert actual.pop("Material") == EXAMPLE_MATERIAL
    expected.pop("Material")
    assert list(actual.items()) == list(expected.items())
    assert template.base_return == custom.base_return


def test_unknown_material_returns_a_copy_of_base_return():
    template = load_template("material")
    first = template.Material("__missing__")
    first["muR"] = 123
    assert template.Material("__missing__")["muR"] == 0
    assert template.base_return["muR"] == 0
