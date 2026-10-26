# File menu examples

Examples of the JSON files that MAGNETISiM 2.1 saves and opens from its **File** menu. They are one
coherent project, saved by the application itself: a Ferroxcube E5.3/2.7/2 core (E family) in 3C98 with a
round-wire copper winding (two layers of 10 turns on each outer leg). Open them in MAGNETISiM to see the
format, or edit a copy and open it back.

Use them to **share a design** (a workspace is one small file you can send or attach to an issue) or to
**load a core of your own without creating a userLib** (edit the dimensions of `Core.json` and open it).
To keep your cores in the program for good, use a user library instead: see the
[core library guide](../../docs/core-library.md) and [`Template/Manufacturer/`](../Manufacturer).

## The files

The shortcuts are two-step chords: press `Ctrl+S` (or `Ctrl+O`), release, then press the letter.

| File | What it holds | Save: File menu and shortcut | Open: File menu and shortcut |
| :--- | :--- | :--- | :--- |
| `Core.json` | Core geometry: manufacturer, family, reference, the dimensions in mm and the gaps. | File > Save Part... > Save Core Geometry Configuration · `Ctrl+S, C` | File > Open Part... > Open Core Geometry Configuration · `Ctrl+O, C` |
| `CoreMat.json` | Core material: permeability and its frequency fit, conductivity, Steinmetz loss coefficients, permittivity. | File > Save Part... > Save Core Material Configuration · `Ctrl+S, M` | File > Open Part... > Open Core Material Configuration · `Ctrl+O, M` |
| `Winding.json` | Winding geometry: conductor type and, for the left, centre and right legs, the clearances, layers, turns and conductor data. | File > Save Part... > Save Winding Geometry Configuration · `Ctrl+S, W` | File > Open Part... > Open Winding Configuration · `Ctrl+O, W` |
| `WindingMat.json` | Winding material: conductor, insulation and coating. | File > Save Part... > Save Winding Material Configuration · `Ctrl+S, L` | File > Open Part... > Open Winding Material Configuration · `Ctrl+O, L` |
| `Workspace.json` | The four files above in one (`DataCoreGeo`, `DataCoreMat`, `DataWindGeo`, `DataWindMat`), plus the excitation typed in the results tab (`DataExcitation`). | File > Save Part... > Save Workspace · `Ctrl+S, A` | File > Open Part... > Open Workspace · `Ctrl+O, A` |
| `MagnetSim.json` | Simulation setup: which simulations run, precision, nominal frequency and the frequency sweep. | File > Save Sim Setup · `Ctrl+S, F` | File > Open Sim Setup · `Ctrl+O, F` |

The project ZIP (File > Save Project, `Ctrl+S, P`, and File > Open Project, `Ctrl+O, P`) also stores the
simulation results, so there is no example of it here.

## Things to know

- **Do not mix them up.** Each Open entry reads the format of its own Save entry. A workspace opened with
  *Open Core Geometry Configuration* is ignored, and a single-part file opened with *Open Workspace* fails
  because the four blocks are missing.
- **`Core.json` always has the ten dimensions** (`A`, `B`, `Bp`, `C`, `Cp`, `D`, `E`, `F`, `G`, `I`), also
  the ones the family does not use, which are `0.0`. The family and the letters are explained in the
  [core library guide](../../docs/core-library.md). `Ae`, `Ve` and `Mass` are not saved.
- **`Gap` is a list `[left, centre, right]`** in mm. In the RZ families it is `[outer, centre, outer]`: a
  third value you type does not count.
- **`CoreType` is saved but not read back**: it comes from the family. If you edit `Core.json` by hand,
  keep a `Manufacturer` and a `MagCore` that exist in the library.
- **Units.** Dimensions, clearances and thicknesses in mm; core conductivity in S/m and winding
  conductivity in MS/m (copper is 58); `NominalFreq`, `f_min` and `f_max` in kHz and `freqRange` in Hz.
- **A leg with no layers** (`Nlayers_Center` is `0` here) has empty lists. Every other list has one value
  per layer.
- **`DataExcitation`** is optional when opening. Its `Connection` is the grouping of the winding the values
  were typed for and `Rows` has one `[type, value]` per group (`v`, `i` or `r`). The values in this example
  are plain numbers to show the format; the application did not write them from a simulation.
