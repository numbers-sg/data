# COE bidding results, every round since 2010

Every Certificate of Entitlement bidding round since January 2010, category by category: the quota premium, quota, bids received and successful, the premium in today's dollars, and the Prevailing Quota Premium for the next month.

**The question it answers:** What did each COE category close at in every bidding round since 2010?

| | |
|---|---|
| Rows | 2,000 |
| Each row | One category in one bidding round |
| Covers | Jan 2010 to Nov 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Land Transport Authority (LTA), via data.gov.sg, Department of Statistics (SingStat) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/cars/coe-results/](https://numbers.sg/cars/coe-results/) |

## Download

- CSV: [`coe-results.csv`](coe-results.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/coe-results/coe-results.csv`
- JSON, with the field list, sources and notices: [`coe-results.json`](coe-results.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/coe-results` (newest rows), `https://numbers.sg/api/v1/coe-results/history` (every row), `https://numbers.sg/api/v1/coe-results.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/coe-results/coe-results.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/coe-results/coe-results.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/coe-results.csv")`

## The last row

| Field | Value |
|---|---|
| `month` | 2026-11 |
| `round` | 2 |
| `closing_date` | 2026-11-18 |
| `category` | E |
| `quota_premium_sgd` | 136000 |
| `quota` | 266 |
| `successful_bids` | 225 |
| `bids_received` | 466 |
| `premium_in_latest_cpi_month_sgd` | 136000 |
| `pqp_for_next_month_sgd` | (empty) |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `month` | month | The month of the bidding exercise. |
| `round` | integer | The round in that month: 1 or 2. Unit: round number. |
| `closing_date` | date | The day bidding closed; from January 2024. Empty when the source gave no figure. |
| `category` | string | COE category: A (smaller cars), B (larger cars), C (goods vehicles and buses), D (motorcycles), E (open). |
| `quota_premium_sgd` | integer | The quota premium: what every successful bidder in the category pays. Unit: S$. |
| `quota` | integer | How many COEs were on offer. Unit: COEs. |
| `successful_bids` | integer | How many bids won a COE. Unit: bids. |
| `bids_received` | integer | How many bids were made. Unit: bids. |
| `premium_in_latest_cpi_month_sgd` | integer | The quota premium in today's money, using SingStat's CPI for the latest month; the month is in the CSV column's name. Unit: S$, in the prices of the month named in the CSV header. |
| `pqp_for_next_month_sgd` | integer | The Prevailing Quota Premium for renewing a COE next month: the mean of the last six rounds' premiums, rounded up. Given on each month's second round for categories A to D, from March 2010. Unit: S$. Empty when it does not apply to that row. |

## Where the numbers come from

- [Land Transport Authority (LTA), via data.gov.sg](https://www.lta.gov.sg/), under the [Singapore Open Data Licence v1.0](https://data.gov.sg/open-data-licence)
- [Department of Statistics (SingStat)](https://www.singstat.gov.sg/), under the [SingStat terms of use](https://www.singstat.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/cars/coe-results/#method](https://numbers.sg/cars/coe-results/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/coe-results/changes.atom`](https://numbers.sg/api/v1/coe-results/changes.atom).

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Land Transport Authority, via data.gov.sg and Department of Statistics, compiled by Numbers.sg (numbers.sg/cars/coe-results/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from COE Bidding Results / Prices (Land Transport Authority) accessed on 2026-11-27 from Land Transport Authority, via data.gov.sg which is made available under the terms of the Singapore Open Data Licence version 1.0 (https://data.gov.sg/open-data-licence)

> Source: Singapore Department of Statistics

To cite it:

```
Numbers.sg (2026). COE bidding results, every round since 2010 [Data set]. https://numbers.sg/cars/coe-results/
```

```bibtex
@misc{numberssg_coe_results,
  author = {{Numbers.sg}},
  title = {{COE bidding results, every round since 2010}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/cars/coe-results/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/coe-results/as-of/YYYY-MM-DD`.
