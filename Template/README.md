# Templates

Starting points to create your own data for MAGNETISiM and to share designs. Everything in this folder is
licensed under [CC BY-NC-SA 4.0](../LICENSE): free for non-commercial use.

| Folder | What it is for |
| :--- | :--- |
| [`Manufacturer/`](Manufacturer) | The two files of a manufacturer for your user library (userLib): `geometry.py` with one example reference for each of the 25 core families you can add, and `material.py` with one example material. Copy them into `core/<YourManufacturer>/`, rename the examples and replace their values with your datasheet values. Dimension letters and units are in the [core library guide](../docs/core-library.md). |
| [`Materials/`](Materials) | Empty Excel templates for the datasheet curves that MAGNETISiM fits to create a core material: core loss against flux density and permeability against frequency. See its [README](Materials/README.md). |
| [`FileOpenSave/`](FileOpenSave) | Examples of the JSON files that MAGNETISiM 2.1 saves and opens from its File menu: core, core material, winding, winding material, workspace and simulation setup. Use them to share a design or to load a core of your own without a userLib. See its [README](FileOpenSave/README.md). |

## How they fit together

1. Read the curves of your material off its datasheet into the spreadsheets of `Materials/` and fit them
   in MAGNETISiM; copy the fitted values into the example material of `Manufacturer/material.py`.
2. Copy the dimensions of each core from its datasheet into `Manufacturer/geometry.py`, using the
   [core library guide](../docs/core-library.md) to match the letters of the datasheet to the ones of
   MAGNETISiM.
3. Put the folder in the `core` folder of your user library. The files in `FileOpenSave/` show what
   MAGNETISiM writes when you save a design with your cores and materials.

The existing manufacturers are in [`lib/core/`](../lib/core).
