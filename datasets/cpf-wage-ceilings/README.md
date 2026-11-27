# CPF Ordinary Wage ceiling, since 1955

[![Chart of CPF Ordinary Wage ceiling, since 1955, from Numbers.sg](https://numbers.sg/charts/cpf-contribution-rates-chart.png)](https://numbers.sg/rates/cpf-contribution-rates/)

The Ordinary Wage ceiling, the most monthly pay CPF contributions are worked out on, for every change since July 1955.

**The question it answers:** What is the most monthly pay CPF contributions are counted on, and how has it changed?

| | |
|---|---|
| Rows | 46 |
| Each row | One ceiling from one date |
| Covers | Jul 1955 to Jan 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Central Provident Fund Board, via data.gov.sg |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/rates/cpf-contribution-rates/](https://numbers.sg/rates/cpf-contribution-rates/) |

## Download

- CSV: [`cpf-wage-ceilings.csv`](cpf-wage-ceilings.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/cpf-wage-ceilings/cpf-wage-ceilings.csv`
- JSON, with the field list, sources and notices: [`cpf-wage-ceilings.json`](cpf-wage-ceilings.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/cpf-wage-ceilings` (newest rows), `https://numbers.sg/api/v1/cpf-wage-ceilings/history` (every row), `https://numbers.sg/api/v1/cpf-wage-ceilings.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/cpf-wage-ceilings/cpf-wage-ceilings.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/cpf-wage-ceilings/cpf-wage-ceilings.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/cpf-wage-ceilings.csv")`

## The last row

| Field | Value |
|---|---|
| `from` | 2026-01 |
| `ordinary_wage_ceiling_sgd` | 8000 |
| `source` | https://data.gov.sg/datasets/d_fcf9b47a2df0c9183875bbfb1c370077/view |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `from` | month | The month this ceiling took effect. |
| `ordinary_wage_ceiling_sgd` | number | Pay above this in a month earns no CPF contributions. Unit: S$ a month. |
| `source` | url | The CPF Board document or data.gov.sg dataset the row is taken from. |

## Where the numbers come from

- [Central Provident Fund Board, via data.gov.sg](https://data.gov.sg/datasets/d_98ffa142ae0dec40391f78f81d26aca9/view), under the [Singapore Open Data Licence v1.0](https://data.gov.sg/open-data-licence)

How each figure is read and checked: [numbers.sg/rates/cpf-contribution-rates/#method](https://numbers.sg/rates/cpf-contribution-rates/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/cpf-wage-ceilings/changes.atom`](https://numbers.sg/api/v1/cpf-wage-ceilings/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **7 Nov 2026:** CPF contribution rates: the lists headed “every change” and “changes” counted years where CPF’s dataset repeats a row and nothing moved. The rates and ceilings were right. Both lists now leave out the repeats, and the note says which rate the “55 and below” column shows.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Central Provident Fund Board, via data.gov.sg, compiled by Numbers.sg (numbers.sg/rates/cpf-contribution-rates/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from CPF Ordinary Wage ceiling, since 1955 accessed on 2026-11-27 from Central Provident Fund Board, via data.gov.sg which is made available under the terms of the Singapore Open Data Licence version 1.0 (https://data.gov.sg/open-data-licence)

To cite it:

```
Numbers.sg (2026). CPF Ordinary Wage ceiling, since 1955 [Data set]. https://numbers.sg/rates/cpf-contribution-rates/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_cpf_wage_ceilings,
  author = {{Numbers.sg}},
  title = {{CPF Ordinary Wage ceiling, since 1955}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/rates/cpf-contribution-rates/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/cpf-wage-ceilings/as-of/YYYY-MM-DD`.
