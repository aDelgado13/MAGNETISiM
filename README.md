<div align="center">
  <img src="./logoabout.png" alt="MAGNETISiM Logo" width="300"/>

  # MAGNETISiM

  *A modular platform for fast, reproducible electromagnetic modeling for education, research, and industry.*

  [![Website](https://img.shields.io/badge/Website-magnetisim.com-blue?style=flat-square)](https://www.magnetisim.com)
  [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
  [![Checks](https://github.com/aDelgado13/MAGNETISiM/actions/workflows/checks.yml/badge.svg)](https://github.com/aDelgado13/MAGNETISiM/actions/workflows/checks.yml)
</div>

---

## What is MAGNETISiM?

MAGNETISiM is a desktop application for designing and simulating magnetic components: it runs finite element simulations with FEMM in the background, computes losses and parasitics, and exports circuit models to SPICE through SPICESiM.
Website: [www.magnetisim.com](https://www.magnetisim.com) · Download: [www.magnetisim.com/download](https://www.magnetisim.com/download)

## What this repository is (and is not)

**It is** the community side of MAGNETISiM:

- the core and material library (`lib/core/`), so that anyone can correct values or propose new references;
- templates to build your own user library (userLib);
- converters to produce library files from spreadsheets and from the files MAGNETISiM saves (in preparation);
- the place to report bugs and request features, through [GitHub issues](https://github.com/aDelgado13/MAGNETISiM/issues/new/choose).

**It is not** the application's source code, which is not published here. The application is free of charge and is distributed under its own End User License Agreement (EULA), shown when you install it.

## Requirements of the application

- Windows 10 or 11 (x64 and ARM64).
- [FEMM 4.2](https://www.femm.info), installed by the user or as a portable copy.
- About 1 GB of disk space once unzipped.
- Unzip it in a folder with a short path (for example `C:\MAGNETISiM`): the application checks the length of its folder at startup.
- The executable is not signed yet, so Windows SmartScreen may show a warning the first time.

## Contents of this repository

| Folder | Contents | License |
| :--- | :--- | :--- |
| [`lib/core/`](lib/core) | Core geometries (`geometry.py`) and materials (`material.py`) in 7 manufacturer folders (AirCore, CustomCore, Ferroxcube, IPT, MagInc, Micrometals, TDK): 29 core families, 664 core references and 175 materials. It is an export of the library shipped with the application and may lag behind its latest release. | CC BY-NC-SA 4.0 |
| [`Template/`](Template) | Templates for your own data: see its [README](Template/README.md). | CC BY-NC-SA 4.0 |
| [`Template/Manufacturer/`](Template/Manufacturer) | `geometry.py` and `material.py` to start a manufacturer of your own: one example reference for each of the 25 core families and one example material. | CC BY-NC-SA 4.0 |
| [`Template/Materials/`](Template/Materials) | Empty spreadsheets for material data: power loss vs. flux density (one file per frequency) and permeability vs. frequency. | CC BY-NC-SA 4.0 |
| [`Template/FileOpenSave/`](Template/FileOpenSave) | Examples of the JSON files MAGNETISiM saves and opens from its File menu (core, core material, winding, winding material, workspace and simulation setup). | CC BY-NC-SA 4.0 |
| [`.github/`](.github) | Issue forms and the pull request template. | CC BY-NC-SA 4.0 |
| [`tests/`](tests) | Checks on the repository content (`pytest`). | PolyForm Noncommercial 1.0.0 |

Core library guide: [`docs/core-library.md`](docs/core-library.md)

## Using a user library (userLib)

MAGNETISiM can load a user library (userLib) next to its built-in library, so you can add your own core references and materials without changing the application. A userLib contains Python files that the application runs, so only load libraries from sources you trust. The templates in [`Template/`](Template) are the starting point; a full guide is coming.

## Reporting issues and contributing

- Found a bug? Use the [bug report form](https://github.com/aDelgado13/MAGNETISiM/issues/new?template=bug_report.yml).
- Missing a feature? Use the [feature request form](https://github.com/aDelgado13/MAGNETISiM/issues/new?template=feature_request.yml).
- A core reference or material is missing or wrong? Use the [core or material data form](https://github.com/aDelgado13/MAGNETISiM/issues/new?template=core_data.yml), or open a pull request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before sending data: MAGNETISiM uses its own dimension convention.

## License

- The MAGNETISiM application is free of charge and is distributed under its own EULA (it is not in this repository).
- The core and material library, templates and documentation in this repository are under [CC BY-NC-SA 4.0](LICENSE); the code of the tools (converters, scripts, tests) is under [PolyForm Noncommercial 1.0.0](LICENSE-CODE).
- Why: this repository exists so that the community can help improve MAGNETISiM, which is free. It can be used, copied and modified for non-commercial purposes, citing MAGNETISiM and the Universidad Politécnica de Madrid (UPM), but not used commercially or to build other products.
- Copies of this repository obtained before 23 October 2026 were published under GPL-3.0; that licence still applies to those copies.

## Authors and affiliation

MAGNETISiM is developed at CEIMM, ETSI Industriales, Universidad Politécnica de Madrid (UPM).

Authors: Alberto Delgado, Alberto Vital, Daniel Ríos, Pedro Alou, Miroslav Vasić, Regina Ramos.

---
<div align="center">
  <i>MAGNETISiM</i><br>
  <b><a href="https://www.magnetisim.com">www.magnetisim.com</a></b>
</div>
