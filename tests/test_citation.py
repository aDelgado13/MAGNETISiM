"""Checks on CITATION.cff, the file GitHub reads for "Cite this repository"."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CITATION = ROOT / "CITATION.cff"
AUTHORS = [
    ("Alberto", "Delgado"),
    ("Alberto", "Vital"),
    ("Daniel", "Ríos"),
    ("Pedro", "Alou"),
    ("Miroslav", "Vasić"),
    ("Regina", "Ramos"),
]


def load():
    return yaml.safe_load(CITATION.read_bytes().decode("utf-8"))


def test_citation_is_cff_1_2_0_with_the_basic_fields():
    data = load()
    assert data["cff-version"] == "1.2.0"
    assert data["message"]
    assert data["title"] == "MAGNETISiM community library"
    assert data["license"] == "CC-BY-NC-SA-4.0"
    assert data["url"] == "https://www.magnetisim.com"
    assert data["repository-code"] == "https://github.com/aDelgado13/MAGNETISiM"


def test_authors_are_those_of_the_readme_in_the_same_order():
    data = load()
    assert [(a["given-names"], a["family-names"]) for a in data["authors"]] == AUTHORS
    assert all(a["affiliation"] == "Universidad Politécnica de Madrid" for a in data["authors"])
    readme = (ROOT / "README.md").read_bytes().decode("utf-8")
    line = next(x for x in readme.splitlines() if x.startswith("Authors: "))
    assert line == "Authors: " + ", ".join(f"{given} {family}" for given, family in AUTHORS) + "."


def test_the_license_is_the_one_of_the_license_file():
    text = (ROOT / "LICENSE").read_bytes().decode("utf-8")
    assert "Attribution-NonCommercial-ShareAlike 4.0 International" in text


def test_preferred_citation_is_the_espc_2026_paper():
    paper = load()["preferred-citation"]
    assert paper["type"] == "conference-paper"
    assert paper["title"] == (
        "Core and Winding Modeling in MAGNETISiM: a Platform For Fast Prototyping of "
        "Magnetic Components"
    )
    assert [(a["given-names"], a["family-names"]) for a in paper["authors"]] == [
        ("Alberto", "Vital"),
        ("Alberto", "Delgado"),
    ]
    assert paper["collection-title"] == "14th European Space Power Conference (ESPC 2026)"
    assert paper["conference"]["name"] == "14th European Space Power Conference (ESPC 2026)"
    assert paper["conference"]["city"] == "Estoril"
    assert paper["conference"]["country"] == "PT"
    assert paper["year"] == 2026


def test_citation_uses_lf():
    assert b"\r" not in CITATION.read_bytes()
