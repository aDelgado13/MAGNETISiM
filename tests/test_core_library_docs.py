"""Checks on the core library guide, its figures and the README of lib/core."""

import importlib.util
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "lib" / "core"
GUIDE = ROOT / "docs" / "core-library.md"
IMAGES = ROOT / "docs" / "images"
MANUFACTURERS = ["AirCore", "CustomCore", "Ferroxcube", "IPT", "MagInc", "Micrometals", "TDK"]
PUBLIC_DOCS = [
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    GUIDE,
    CORE / "README.md",
    ROOT / "Template" / "README.md",
    ROOT / "Template" / "Materials" / "README.md",
    ROOT / "Template" / "FileOpenSave" / "README.md",
]
LINK_PATTERNS = [
    re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)"),
    re.compile(r'(?:src|href)="([^"]+)"'),
]
SVG = "{http://www.w3.org/2000/svg}"


def read(path):
    return path.read_bytes().decode("utf-8")


def block(text, name):
    match = re.search(rf"<!-- {name}:start -->\n(.*?)<!-- {name}:end -->", text, flags=re.DOTALL)
    assert match, name
    return match.group(1)


def load_module(man, kind):
    path = CORE / man / f"{kind}.py"
    spec = importlib.util.spec_from_file_location(f"core_docs_test_{man}_{kind}", path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def library():
    """Return ({family: CoreType}, number of references, number of materials) from the code."""
    types, references, materials = {}, 0, 0
    for man in MANUFACTURERS:
        geometry = load_module(man, "geometry")
        for name in dir(geometry):
            function = getattr(geometry, name)
            if name.endswith("Geometry") and callable(function):
                family = name[: -len("Geometry")]
                types.setdefault(family, set()).add(function(None, True))
                references += len(function(None, False))
        materials += len(load_module(man, "material").Material(None))
    return types, references, materials


def index_rows(text):
    """Return [(families, model)] from the table between the core-index markers."""
    rows = []
    for line in block(text, "core-index").splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Family"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append(([name.strip() for name in cells[0].split(",")], cells[1]))
    return rows


def expected_model(core_type):
    return core_type[0] + (" + plate" if core_type[2] == "WITH_I" else "")


def github_anchors(text):
    """Anchors GitHub gives to the headings: lowercase, no punctuation, hyphens for spaces."""
    anchors, seen = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*$", text, flags=re.MULTILINE):
        title = re.sub(r"\[([^\]]*)\]\([^)]*\)", lambda match: match.group(1), title)
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


def link_targets(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    for pattern in LINK_PATTERNS:
        yield from pattern.findall(text)


def relative_links(doc):
    for target in link_targets(read(doc)):
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("mailto:", "//")):
            continue
        yield target, unquote(parsed.path), parsed.fragment


def guide_images(text):
    return {Path(target).name for target in re.findall(r"!\[[^\]]*\]\(images/([^)\s]+)\)", text)}


# --- the index and the counts against the code ----------------------------------


def test_every_family_has_one_core_type_in_the_code():
    types, _, _ = library()
    assert len(types) == 29
    assert all(len(value) == 1 for value in types.values()), types


def test_guide_index_matches_the_core_types():
    types, _, _ = library()
    listed = {}
    for families, model in index_rows(read(GUIDE)):
        for family in families:
            assert family not in listed, f"{family} appears twice in the index"
            listed[family] = model
    assert set(listed) == set(types)
    for family, core_type in types.items():
        assert listed[family] == expected_model(next(iter(core_type))), family


def test_core_readme_counts_match_the_code():
    types, references, materials = library()
    line = block(read(CORE / "README.md"), "library-counts").strip()
    assert line.startswith(
        f"{len(types)} core families, {references} references and {materials} materials"
    )


# --- figures ----------------------------------------------------------------------


def test_the_guide_links_the_figures_that_exist_and_none_is_orphan():
    used = guide_images(read(GUIDE))
    on_disk = {path.name for path in IMAGES.iterdir()}
    assert used - on_disk == set(), "linked figures that do not exist"
    assert on_disk - used == set(), "figures that the guide does not use"
    assert len(on_disk) == 17


def svg_files():
    return sorted(IMAGES.glob("*.svg"))


@pytest.mark.parametrize("path", svg_files(), ids=lambda p: p.name)
def test_svg_is_valid_and_self_contained(path):
    text = read(path)
    root = ET.fromstring(text)
    assert root.tag == f"{SVG}svg"
    assert root.get("viewBox")
    titles = [child for child in root if child.tag == f"{SVG}title"]
    assert titles and (titles[0].text or "").strip()
    first_rect = next(root.iter(f"{SVG}rect"))
    assert first_rect.get("fill") == "#FFFFFF", "the first <rect> must be the white background"
    assert not re.search(r"""href=["']http""", text)
    assert "<image" not in text
    assert "\r" not in text


# --- links ------------------------------------------------------------------------


@pytest.mark.parametrize("doc", PUBLIC_DOCS, ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_point_to_existing_files(doc):
    assert doc.is_file()
    for _, path, _ in relative_links(doc):
        if path:
            assert (doc.parent / path).exists(), f"{doc.name}: {path}"


def test_guide_anchors_point_to_existing_headings():
    text = read(GUIDE)
    anchors = github_anchors(text)
    targets = [t for t in link_targets(text) if t.startswith("#")]
    assert len(targets) > 10
    for target in targets:
        assert target[1:] in anchors, target
    for _, path, fragment in relative_links(GUIDE):
        assert not (fragment and path), "anchors into other files are not checked"


def test_anchor_rule_follows_github():
    text = "# A: b `c`\n## Same\n## Same\n"
    assert github_anchors(text) == {"a-b-c", "same", "same-1"}


def test_the_guide_is_linked_from_readme_and_contributing():
    for name in ("README.md", "CONTRIBUTING.md"):
        text = read(ROOT / name)
        assert "(docs/core-library.md)" in text, name
    assert "Core library guide: [`docs/core-library.md`](docs/core-library.md)" in read(
        ROOT / "README.md"
    )
    assert "in preparation" not in read(ROOT / "CONTRIBUTING.md")


# --- public text ------------------------------------------------------------------


@pytest.mark.parametrize("path", PUBLIC_DOCS + svg_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_markdown_and_svg_use_lf(path):
    assert b"\r" not in path.read_bytes()
