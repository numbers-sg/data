# Singapore resident income tax rates

IRAS's progressive income tax rates for tax residents, band by band: where each band starts and ends, its rate, the tax on the whole band and the total tax up to its top, for Year of Assessment 2024 onwards.

**The question it answers:** What are Singapore's resident income tax rates, band by band?

| | |
|---|---|
| Rows | 13 |
| Each row | One band of chargeable income |
| Covers | Today’s figures (not a time series) |
| Rows last changed here | 27 Nov 2026 |
| Source | Singapore Statutes Online: Income Tax Act 1947 |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/tax/income-tax-rates/](https://numbers.sg/tax/income-tax-rates/) |

## Download

- CSV: [`income-tax-rates.csv`](income-tax-rates.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/income-tax-rates/income-tax-rates.csv`
- JSON, with the field list, sources and notices: [`income-tax-rates.json`](income-tax-rates.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/income-tax-rates` (newest rows), `https://numbers.sg/api/v1/income-tax-rates/history` (every row), `https://numbers.sg/api/v1/income-tax-rates.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/income-tax-rates/income-tax-rates.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/income-tax-rates/income-tax-rates.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/income-tax-rates.csv")`

## The last row

| Field | Value |
|---|---|
| `band` | 13 |
| `from_sgd` | 1000000 |
| `to_sgd` | (empty) |
| `rate_pct` | 24 |
| `tax_on_band_sgd` | (empty) |
| `tax_up_to_band_top_sgd` | (empty) |
| `applies` | YA 2024 onwards (YA 2026, YA 2027) |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `band` | integer | The band, from the lowest income up. Unit: band number. |
| `from_sgd` | integer | Where the band starts. Unit: S$ of chargeable income a year. |
| `to_sgd` | integer | Where the band ends; blank (the CSV says no limit) for the top band. Unit: S$ of chargeable income a year. Empty when it does not apply to that row. |
| `rate_pct` | number | The tax rate on the part of chargeable income in this band. Unit: percent of the income in this band. |
| `tax_on_band_sgd` | integer | The tax on the whole band; blank for the open-ended top band. Unit: S$. Empty when it does not apply to that row. |
| `tax_up_to_band_top_sgd` | integer | The total tax on chargeable income up to the top of this band. Unit: S$. Empty when it does not apply to that row. |
| `applies` | string | The Years of Assessment these rates apply to, in IRAS's terms. |

## Where the numbers come from

- [Singapore Statutes Online: Income Tax Act 1947](https://sso.agc.gov.sg/Act/ITA1947), under the [Singapore Statutes Online: permission to reproduce legislation](https://sso.agc.gov.sg/Terms-of-Use)

How each figure is read and checked: [numbers.sg/tax/income-tax-rates/#method](https://numbers.sg/tax/income-tax-rates/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/income-tax-rates/changes.atom`](https://numbers.sg/api/v1/income-tax-rates/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Singapore Statutes Online: Income Tax Act 1947, compiled by Numbers.sg (numbers.sg/tax/income-tax-rates/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Singapore legislation is subject to copyright of the Singapore Government and is reproduced with the permission of the Attorney-General’s Chambers; check Singapore Statutes Online (sso.agc.gov.sg) for the latest version.

To cite it:

```
Numbers.sg (2026). Singapore resident income tax rates [Data set]. https://numbers.sg/tax/income-tax-rates/
```

```bibtex
@misc{numberssg_income_tax_rates,
  author = {{Numbers.sg}},
  title = {{Singapore resident income tax rates}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/tax/income-tax-rates/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/income-tax-rates/as-of/YYYY-MM-DD`.
