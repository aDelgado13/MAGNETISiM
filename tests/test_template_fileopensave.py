"""Checks on Template/FileOpenSave: examples of the JSON files of the File menu (2.1)."""

import json
import re
import subprocess
from pathlib import Path

import pytest
from test_lib_core import load_module

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "Template" / "FileOpenSave"
README = FOLDER / "README.md"

# Keys measured on 23/10/2026. Source of the files: the example project E (Ferroxcube
# E5.3/2.7/2) saved with MAGNETISiM 2.1; the same keys are in the other four example projects
# measured (EPlanar, EQ, PQI and U: XY and RZ, with and without plate, Round and PCB), so they
# do not change with the core. Writers (bin/barFunctions/File.py of the application):
# Core.json = fn_saveMagCoreParametersJSON, CoreMat.json = fn_saveMagMatParametersJSON,
# Winding.json = fn_saveWindingParametersJSON, WindingMat.json = fn_saveWindingMatParametersJSON,
# Workspace.json = fn_saveWorkSpaceParametersJSON, MagnetSim.json = fn_SaveSetupParametersJSON.
LEGS = ("Left", "Center", "Right")
WINDING_FIELDS = (
    "ClearanceXY",
    "ClearanceZ",
    "Nlayers",
    "LayerPitch",
    "Distribution",
    "Nturns",
    "CopperThickness",
    "WidthCopper",
    "CopperRadius",
    "StrandRadius",
    "StrandNumber",
    "PackingFactor",
    "Pitch",
    "Edge",
)
DEBYE = [{"Real": ["y0", "A", "k", "xc"]}, {"Imag": ["a1", "b1", "c1", "a2", "b2", "c2"]}]
SHAPES = {
    "Core.json": [
        "Manufacturer",
        "MagCore",
        "Reference",
        "A",
        "B",
        "Bp",
        "C",
        "Cp",
        "D",
        "E",
        "F",
        "G",
        "I",
        "Gap",
        "CoreType",
    ],
    "CoreMat.json": [
        "Material",
        "muR",
        "muI",
        "Cond",
        "FreqCurveMu",
        {"DebyeParameter": DEBYE},
        "Phi",
        "Bmax",
        {"Steinmetz": ["k", "alpha", "beta"]},
        "epsR",
        "tanDelta",
    ],
    "Winding.json": ["ConductorType"]
    + [f"{field}_{leg}" for field in WINDING_FIELDS for leg in LEGS],
    "WindingMat.json": [
        "Material",
        "muR",
        "muI",
        "Cond",
        "Phi",
        "FreqCurveEps",
        {"Insulation": ["Material", "epsR", "tanDelta", "DebyeEps"]},
        {"Coating": ["Material", "epsR", "tanDelta", "Thickness", "DebyeEps"]},
    ],
    "MagnetSim.json": [
        "SimName",
        "MagnetCheck",
        "ElectricalCheck",
        "ThermalCheck",
        "maxErrorMagnet",
        "NominalFreq",
        "maxErrorElectrical",
        "CoreGrounded",
        "IncludeLosses",
        "maxErrorThermal",
        "ACType",
        "SweepType",
        "f_min",
        "f_max",
        "n_points",
        "NomIncluded",
        "listFreq",
        "WaveformAC",
        "nHarm",
        "freqRange",
    ],
}
WORKSPACE_BLOCKS = {
    "DataCoreGeo": "Core.json",
    "DataCoreMat": "CoreMat.json",
    "DataWindGeo": "Winding.json",
    "DataWindMat": "WindingMat.json",
}
WORKSPACE_KEYS = [*WORKSPACE_BLOCKS, "DataExcitation"]
JSON_FILES = sorted([*SHAPES, "Workspace.json"])

# Menu File of MAGNETISiM 2.1 (bin/gui/mainWindow/titleBar.py): save entry, save shortcut, open
# entry, open shortcut. "Part" entries hang from File > Save Part... and File > Open Part...
MENU = {
    "Core.json": (
        "Save Part... > Save Core Geometry Configuration",
        "Ctrl+S, C",
        "Open Part... > Open Core Geometry Configuration",
        "Ctrl+O, C",
    ),
    "CoreMat.json": (
        "Save Part... > Save Core Material Configuration",
        "Ctrl+S, M",
        "Open Part... > Open Core Material Configuration",
        "Ctrl+O, M",
    ),
    "Winding.json": (
        "Save Part... > Save Winding Geometry Configuration",
        "Ctrl+S, W",
        "Open Part... > Open Winding Configuration",
        "Ctrl+O, W",
    ),
    "WindingMat.json": (
        "Save Part... > Save Winding Material Configuration",
        "Ctrl+S, L",
        "Open Part... > Open Winding Material Configuration",
        "Ctrl+O, L",
    ),
    "Workspace.json": (
        "Save Part... > Save Workspace",
        "Ctrl+S, A",
        "Open Part... > Open Workspace",
        "Ctrl+O, A",
    ),
    "MagnetSim.json": ("Save Sim Setup", "Ctrl+S, F", "Open Sim Setup", "Ctrl+O, F"),
}
CORE_TYPES = [("XY", "RZ"), ("1LEG", "2LEG", "3LEG"), ("SET", "WITH_I")]
OLD_KEYS = ("Steinmetzk", "SteinmetzA", "SteinmetzB", "maxError")


def read_json(name):
    return json.loads((FOLDER / name).read_bytes().decode("utf-8"))


def key_tree(data):
    """Keys in order; an object inside an object becomes a one-key dict, as in SHAPES."""
    return [
        {key: key_tree(value)} if isinstance(value, dict) else key for key, value in data.items()
    ]


# --- the folder --------------------------------------------------------------------


def test_folder_holds_exactly_the_json_files_and_the_readme():
    names = sorted(p.name for p in FOLDER.iterdir())
    assert names == sorted([*JSON_FILES, "README.md"])


def test_no_zip_files_in_the_repository():
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split("\n")
    assert [p for p in out if p.lower().endswith((".zip", ".7z", ".rar"))] == []


# --- the files ---------------------------------------------------------------------


@pytest.mark.parametrize("name", JSON_FILES)
def test_json_is_valid_and_written_as_the_application_writes_it(name):
    text = (FOLDER / name).read_bytes().decode("utf-8")
    data = json.loads(text)
    assert isinstance(data, dict)
    assert json.dumps(data, indent=4, ensure_ascii=False) == text.replace("\r\n", "\n").rstrip("\n")


@pytest.mark.parametrize("name", sorted(SHAPES))
def test_keys_are_those_the_2_1_writes(name):
    data = read_json(name)
    assert key_tree(data) == SHAPES[name]
    assert not set(OLD_KEYS) & set(data)


def test_workspace_has_the_four_blocks_and_the_excitation():
    workspace = read_json("Workspace.json")
    assert list(workspace) == WORKSPACE_KEYS
    for block, name in WORKSPACE_BLOCKS.items():
        assert key_tree(workspace[block]) == SHAPES[name], block


def test_workspace_blocks_are_the_content_of_the_single_files():
    workspace = read_json("Workspace.json")
    for block, name in WORKSPACE_BLOCKS.items():
        assert workspace[block] == read_json(name), block


def test_excitation_has_the_connection_and_one_row_per_group():
    excitation = read_json("Workspace.json")["DataExcitation"]
    assert list(excitation) == ["Connection", "Rows"]
    assert len(excitation["Connection"]) == len(excitation["Rows"])
    assert all(len(row) == 2 and row[0] in {"v", "i", "r"} for row in excitation["Rows"])
    assert all(isinstance(value, str) for row in excitation["Rows"] for value in row)


# --- the project is coherent and is a real library core -----------------------------


def test_core_is_a_reference_of_lib_core_with_the_same_dimensions():
    core = read_json("Core.json")
    geometry = getattr(load_module(core["Manufacturer"], "geometry"), f"{core['MagCore']}Geometry")
    assert core["Reference"] in geometry(None, False)
    reference = geometry(core["Reference"], False)
    parameters = geometry("GeoParam", False)
    for key in ("A", "B", "Bp", "C", "Cp", "D", "E", "F", "G", "I"):
        assert core[key] == (reference[key] if key in parameters else 0.0), key
    assert tuple(core["CoreType"]) == geometry(None, True)
    assert all(value in group for value, group in zip(core["CoreType"], CORE_TYPES))


def test_gap_is_a_list_of_three_values():
    gap = read_json("Core.json")["Gap"]
    assert isinstance(gap, list) and len(gap) == 3
    assert all(isinstance(value, float) for value in gap)


def test_core_material_is_the_one_of_lib_core():
    material = read_json("CoreMat.json")
    manufacturer = read_json("Core.json")["Manufacturer"]
    library = load_module(manufacturer, "material").Material(material["Material"])
    for key in ("muR", "muI", "Cond", "DebyeParameter", "Phi", "Steinmetz", "epsR", "tanDelta"):
        assert material[key] == library[key], key


def test_winding_lists_have_one_value_per_layer():
    winding = read_json("Winding.json")
    for leg in LEGS:
        layers = winding[f"Nlayers_{leg}"]
        assert isinstance(layers, int)
        for field in WINDING_FIELDS:
            value = winding[f"{field}_{leg}"]
            if field in {"ClearanceXY", "ClearanceZ", "Nlayers", "Distribution"}:
                assert not isinstance(value, list), (field, leg)
            else:
                assert len(value) == layers, (field, leg)


def test_winding_material_has_the_electrical_data():
    material = read_json("WindingMat.json")
    assert material["Material"] == "Copper"
    assert material["Insulation"]["DebyeEps"] is None
    assert material["Coating"]["DebyeEps"] is None


def test_setup_frequencies_are_consistent():
    setup = read_json("MagnetSim.json")
    assert setup["ACType"] in {"Frequency Range", "Waveform"}
    assert setup["SweepType"] in {"Nominal", "Logarithmic", "Linear", "List"}
    assert setup["freqRange"] == sorted(setup["freqRange"])
    assert len(setup["freqRange"]) == int(setup["n_points"])


# --- the README ---------------------------------------------------------------------


def readme_text():
    return README.read_bytes().decode("utf-8")


def test_readme_names_every_json_and_no_other():
    named = set(re.findall(r"[\w-]+\.json", readme_text()))
    assert named == set(JSON_FILES)


@pytest.mark.parametrize("name", sorted(MENU))
def test_readme_gives_the_menu_entries_and_shortcuts(name):
    rows = [line for line in readme_text().splitlines() if line.startswith(f"| `{name}`")]
    assert len(rows) == 1, name
    save, save_keys, load, load_keys = MENU[name]
    cells = [cell.strip() for cell in rows[0].strip("|").split("|")]
    assert f"File > {save}" in cells[2] and f"`{save_keys}`" in cells[2], name
    assert f"File > {load}" in cells[3] and f"`{load_keys}`" in cells[3], name


def test_readme_says_what_the_files_are_for():
    text = readme_text()
    assert "share" in text.lower()
    assert "userLib" in text
    assert "../../docs/core-library.md" in text
