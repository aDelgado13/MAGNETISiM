# MAGNETISiM core library

This folder is the library of magnetic cores and core materials that ships with
[MAGNETISiM](https://www.magnetisim.com), the free design and simulation tool for magnetic components
developed at the Universidad Politécnica de Madrid (UPM).

## Why it is public

MAGNETISiM is free, and the library is where the community can help it most. Every value here can be
checked against the manufacturer's datasheet. If you find a wrong dimension, miss a reference or have
fitted a new material, tell us: corrections and additions go into the next version of the application,
for everyone. You can also copy these files as the starting point of your own user library.

## What is inside

| Folder | Content |
|---|---|
| `TDK/`, `Ferroxcube/`, `MagInc/`, `Micrometals/` | Commercial cores (public catalogue dimensions) and their materials |
| `CustomCore/` | Editable example of every family, to define a core that is not in a catalogue |
| `AirCore/`, `IPT/` | Air-core coils and inductive power transfer pads, defined by the MAGNETISiM team |

<!-- library-counts:start -->
29 core families, 664 references and 175 materials (MAGNETISiM 2.1).
<!-- library-counts:end -->

## How the files are organised

- `geometry.py`: one function per core family (`EGeometry`, `PQGeometry`…), with one entry per reference.
  Dimensions in mm, `Ae` in mm², `Ve` in mm³, `Mass` in g.
- `material.py`: one entry per material: permeability, its frequency curve, conductivity and the
  Steinmetz loss coefficients.
- The dimensions follow the **MAGNETISiM convention**, not the catalogue's letters. See the
  [core library guide](../../docs/core-library.md) for a drawing of every family and the meaning of
  every material parameter.

## Use them in your own library

Copy a manufacturer folder into the `core` folder of your user library and edit it. The user library
folder is chosen in MAGNETISiM, in the material part of the core tab. A folder with the same name as a
built-in one appears as *"Name (user)"*, so you can keep both.

## Contribute

Open an issue with the **Core or material data** form, or send a pull request. Add a link to the public
datasheet; do not upload images copied from datasheets. See [CONTRIBUTING](../../CONTRIBUTING.md).

## License

[CC BY-NC-SA 4.0](../../LICENSE): free for non-commercial use, citing MAGNETISiM and the UPM. The
MAGNETISiM application is distributed under its own EULA.
