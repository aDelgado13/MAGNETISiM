# Contributing to MAGNETISiM

Thank you for helping improve the MAGNETISiM core and material library. Contributions are reviewed by the MAGNETISiM team and are included in the application in later releases.

## How to propose a core or a correction

You can do it in two ways:

1. **Open an issue** with the [core or material data form](https://github.com/aDelgado13/MAGNETISiM/issues/new?template=core_data.yml). This is the easiest way and needs no Git.
2. **Open a pull request** that edits the `geometry.py` or `material.py` of the manufacturer in [`lib/core/`](lib/core). Fill in the [pull request template](.github/pull_request_template.md).

For bugs in the application or feature ideas, use the [issue forms](https://github.com/aDelgado13/MAGNETISiM/issues/new/choose) instead.

## Accepted sources

- Every value must come from a **public datasheet** of the manufacturer. Include the link in the issue or pull request.
- **Do not upload images, plots or tables copied from datasheets.** They are protected by copyright. The link is enough: we read the values from the source.

## Dimension convention

MAGNETISiM uses **its own convention for core dimensions. It is not the one used in manufacturer catalogues**: the same letter often means a different dimension. Convert the catalogue values before sending them.

| Letter | Meaning in MAGNETISiM |
| :---: | :--- |
| `A` | Total width |
| `B` | Window opening |
| `Bp` | Actual winding width (RZ geometries) |
| `C` | Centre leg: diameter (RZ) or width (XY) |
| `Cp` | Hole in the centre leg |
| `D` | Height of **half** a core |
| `E` | Window height (of half a core) |
| `F` | Depth that carries the flux |
| `G` | Family-specific: PQ/PQI, width at the bottom of the notch; PM, width at the bottom of the opening; RM, side of the square rotated 45°; EL/ELT, depth of the base (and there `F` is the depth of the centre leg) |
| `I` | Height of the cap (plate) |

Each reference also carries `Ae`, `Ve` and `Mass` from the datasheet, and `Gap`.

Units: all dimensions are in millimetres (mm), with `Ae` in mm², `Ve` in mm³ and `Mass` in g.

The full guide to the library format, with a drawing of every family, is the [core library guide](docs/core-library.md).

## License of contributions

By submitting a contribution (issue, data or pull request) you confirm that you have the right to submit it, you license it under CC BY-NC-SA 4.0 (data and documentation) or PolyForm Noncommercial 1.0.0 (code), and you grant the Universidad Politécnica de Madrid (UPM) a perpetual, worldwide, royalty-free, non-exclusive licence to use, modify and distribute it, including as part of the MAGNETISiM application under its EULA.
