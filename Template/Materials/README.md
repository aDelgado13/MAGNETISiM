# Material templates

Empty Excel templates for the curves that MAGNETISiM fits to create a core material. Fill them with
the curves of the manufacturer's datasheet (read the values off the plot yourself; do not upload
images copied from datasheets), then load them in MAGNETISiM. The fitted values go into an entry of
`material.py` (see the [core library guide](../../docs/core-library.md#how-to-add-a-material)).

## `PowerLoss/`: core loss against flux density

`100kHz_pv.xlsx` is the template for **one frequency**. Make one copy per frequency of the datasheet.

| Column | Header | Content | Unit |
|---|---|---|---|
| A | `BmT` | Peak flux density B | mT |
| B | `Pv` | Core loss per unit volume | kW/m³ |

- Row 1 is the header and the data start in row 2, with at least 4 rows per file.
- **The frequency is read from the file name**: it must contain the number followed by `kHz`
  (`100kHz_pv.xlsx`, `N87_25.5kHz.xlsx`). Rename each copy.
- Only the position of the columns matters: B first, Pv second. Values must be greater than 0 and there
  must be no empty cells.
- In MAGNETISiM: core material panel, **Power Loss** tab, select all the files (one per frequency) and
  fit k, α and β of the Steinmetz equation.

## `PermeabilityFrequency/`: µ′ and µ″ against frequency

`permeability_vs_frequency.xlsx` holds the real and imaginary parts of the permeability.

| Column | Header | Content | Unit |
|---|---|---|---|
| A | `f_Hz` | Frequency | Hz |
| B | `mu_prime` | Real part µ′ | relative |
| C | `mu_doubleprime` | Imaginary part µ″ | relative |

- **Row 1 is a free title and is skipped; the headers are in row 2; the data start in row 3**, with at
  least 4 rows. Do not delete the title row.
- Only the position of the columns matters. The three columns share the same frequencies. Values must be
  greater than 0 and there must be no empty cells.
- In MAGNETISiM: core material panel, **Add Permeability(f) Curve**, select the file and fit.
