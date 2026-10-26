"""Checks on the public documentation (README.md and CONTRIBUTING.md)."""

import hashlib
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ["README.md", "CONTRIBUTING.md"]
# Markdown links/images: [text](target) and ![alt](target); HTML: src="..." and href="...".
LINK_PATTERNS = [
    re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)"),
    re.compile(r'(?:src|href)="([^"]+)"'),
]


def links(text):
    for pattern in LINK_PATTERNS:
        yield from pattern.findall(text)


def relative_targets(doc):
    text = (ROOT / doc).read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    for target in links(text):
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("#", "mailto:", "//")):
            continue
        yield target, unquote(parsed.path)


@pytest.mark.parametrize("doc", DOCS)
def test_document_exists_and_has_relative_links(doc):
    assert (ROOT / doc).is_file()
    assert list(relative_targets(doc)), "expected at least one relative link"


@pytest.mark.parametrize("doc", DOCS)
def test_relative_links_point_to_existing_files(doc):
    broken = [
        target
        for target, path in relative_targets(doc)
        if not (ROOT / doc).parent.joinpath(path).exists()
    ]
    assert broken == []


def public_text_files():
    paths = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    for path in paths:
        if Path(path).suffix.lower() in {".md", ".yml", ".yaml", ".txt", ".json", ".toml"}:
            yield path


def test_no_weekly_builds_promise():
    promising = [
        path
        for path in public_text_files()
        if "weekly build" in (ROOT / path).read_text(encoding="utf-8", errors="ignore").lower()
    ]
    assert promising == []


CC_BADGE = (
    "[![License: CC BY-NC-SA 4.0]"
    "(https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square)]"
    "(https://creativecommons.org/licenses/by-nc-sa/4.0/)"
)
HISTORICAL_GPL = (
    "Copies of this repository obtained before 23 October 2026 were published under GPL-3.0; "
    "that licence still applies to those copies."
)
CONTRIBUTION_GRANT = (
    "By submitting a contribution (issue, data or pull request) you confirm that you have the "
    "right to submit it, you license it under CC BY-NC-SA 4.0 (data and documentation) or "
    "PolyForm Noncommercial 1.0.0 (code), and you grant the Universidad Politécnica de Madrid "
    "(UPM) a perpetual, worldwide, royalty-free, non-exclusive licence to use, modify and "
    "distribute it, including as part of the MAGNETISiM application under its EULA."
)
# SHA-256 of the official texts as downloaded on 23/10/2026 (LF line endings).
CC_LEGALCODE_SHA256 = "e66c269d4819aaab34b49ef5220c4ddab6756f21bb5180761a4eb8561f2b7bbd"
POLYFORM_SHA256 = "c0ea4a896d2c8c394b29f9427589996db826cd501c512279ff0ed3ef48fabbe5"
REQUIRED_NOTICE = "Required Notice: Copyright (c) 2026 Universidad Politécnica de Madrid (UPM)"


def lf_bytes(name):
    return (ROOT / name).read_bytes().replace(b"\r\n", b"\n")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def doc_text(doc):
    return (ROOT / doc).read_text(encoding="utf-8")


def license_section(text):
    return re.search(r"^## License\n(.*?)(?=^## )", text, flags=re.DOTALL | re.MULTILINE).group(1)


def test_license_badge_is_cc_by_nc_sa():
    assert CC_BADGE in doc_text("README.md")


@pytest.mark.parametrize("doc", DOCS)
def test_only_historical_gpl_mention(doc):
    text = doc_text(doc).replace(HISTORICAL_GPL, "")
    assert "GPL" not in text.upper().replace("CC BY-NC-SA", "")


def test_readme_keeps_historical_gpl_sentence():
    assert HISTORICAL_GPL in doc_text("README.md")


def test_readme_license_section_names_both_licenses_and_eula():
    section = license_section(doc_text("README.md"))
    assert "CC BY-NC-SA 4.0" in section
    assert "PolyForm Noncommercial 1.0.0" in section
    assert "EULA" in section
    assert "](LICENSE)" in section and "](LICENSE-CODE)" in section
    assert "non-commercial" in section


def test_contributing_grants_upm_the_right_to_reuse():
    text = doc_text("CONTRIBUTING.md")
    assert CONTRIBUTION_GRANT in text
    assert "Universidad Politécnica de Madrid (UPM)" in text.split("## License of contributions")[1]


def test_license_is_official_cc_by_nc_sa_text():
    assert sha256(lf_bytes("LICENSE")) == CC_LEGALCODE_SHA256


def test_license_code_is_official_polyform_text_plus_required_notice():
    data = lf_bytes("LICENSE-CODE")
    notice = (REQUIRED_NOTICE + "\n").encode("utf-8")
    assert data.endswith(notice)
    body = data[: -len(notice)]
    assert body.endswith(b"\n\n")
    assert sha256(body[:-1]) == POLYFORM_SHA256


def test_readme_links_download_page():
    assert "](https://www.magnetisim.com/download)" in doc_text("README.md")


APP_VERSION = re.compile(
    r"MAGNETISiM\W{0,3}(?:version\s+)?v?\d+\.\d+(?:\.\d+)?|\bv\d+\.\d+|\bversion\s+v?\d+",
    re.IGNORECASE,
)


def test_readme_has_no_application_version():
    text = re.sub(r"<!--.*?-->", "", doc_text("README.md"), flags=re.DOTALL)
    assert APP_VERSION.findall(text) == []


@pytest.mark.parametrize(
    "phrase",
    [
        "Windows 10 or 11 (x64 and ARM64)",
        "FEMM 4.2",
        "About 1 GB of disk space",
        "short path",
        "C:\\MAGNETISiM",
        "SmartScreen",
    ],
)
def test_readme_states_requirements(phrase):
    assert phrase in doc_text("README.md")


def test_contributing_states_units():
    text = doc_text("CONTRIBUTING.md")
    assert "millimetres (mm)" in text
    assert "`Ae` in mm²" in text and "`Ve` in mm³" in text and "`Mass` in g" in text
