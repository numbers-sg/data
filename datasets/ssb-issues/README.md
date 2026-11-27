# Singapore Savings Bonds: rates and results

[![Chart of Singapore Savings Bonds: rates and results, from Numbers.sg](https://numbers.sg/charts/singapore-savings-bonds-rates-chart.png)](https://numbers.sg/rates/singapore-savings-bonds/)

Every Singapore Savings Bond since the first in October 2015: its interest year by year, the average return if you cash it in after each year, the amount offered and applied for, and, when it was oversubscribed, how much each applicant got.

**The question it answers:** What does each Singapore Savings Bond pay, and how was it allotted?

| | |
|---|---|
| Rows | 135 |
| Each row | One Savings Bond issue (one month's bond) |
| Covers | 1 Oct 2015 to 1 Dec 2026 |
| Rows last changed here | 27 Nov 2026 |
| Source | Monetary Authority of Singapore (MAS) |
| Licence | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Live page | [numbers.sg/rates/singapore-savings-bonds/](https://numbers.sg/rates/singapore-savings-bonds/) |

## Download

- CSV: [`ssb-issues.csv`](ssb-issues.csv) · raw: `https://raw.githubusercontent.com/numbers-sg/data/main/datasets/ssb-issues/ssb-issues.csv`
- JSON, with the field list, sources and notices: [`ssb-issues.json`](ssb-issues.json)
- The freshest copy, from the free API (no key), which reads the source on its own schedule: `https://numbers.sg/api/v1/ssb-issues` (newest rows), `https://numbers.sg/api/v1/ssb-issues/history` (every row), `https://numbers.sg/api/v1/ssb-issues.csv`

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/ssb-issues/ssb-issues.csv")
```

```r
df <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/ssb-issues/ssb-issues.csv")
```

In Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/ssb-issues.csv")`

## The last row

| Field | Value |
|---|---|
| `bond` | SBDEC26 |
| `issue_code` | GX26120A |
| `announced` | 2026-11-02 |
| `last_day_to_apply` | 2026-11-25 |
| `allotment_date` | 2026-11-26 |
| `issue_date` | 2026-12-01 |
| `maturity_date` | 2036-12-01 |
| `year1_interest_pct` | 1.83 |
| `year2_interest_pct` | 1.99 |
| `year3_interest_pct` | 2.17 |
| `year4_interest_pct` | 2.35 |
| `year5_interest_pct` | 2.47 |
| `year6_interest_pct` | 2.52 |
| `year7_interest_pct` | 2.57 |
| `year8_interest_pct` | 2.63 |
| `year9_interest_pct` | 2.71 |
| `year10_interest_pct` | 2.83 |
| `avg_return_if_held_1y_pct` | 1.83 |
| `avg_return_if_held_2y_pct` | 1.91 |
| `avg_return_if_held_3y_pct` | 1.99 |
| `avg_return_if_held_4y_pct` | 2.08 |
| `avg_return_if_held_5y_pct` | 2.16 |
| `avg_return_if_held_6y_pct` | 2.21 |
| `avg_return_if_held_7y_pct` | 2.26 |
| `avg_return_if_held_8y_pct` | 2.3 |
| `avg_return_if_held_9y_pct` | 2.34 |
| `avg_return_if_held_10y_pct` | 2.39 |
| `amount_offered_sgd_m` | 500 |
| `applied_within_limits_sgd_m` | 249.9245 |
| `allotted_sgd_m` | 249.9245 |
| `full_allotment_up_to_sgd` | (empty) |
| `random_extra_500_pct` | (empty) |
| `source` | MAS Savings Bonds data; compiled by Numbers.sg |

## Fields

| Field | Type | Meaning |
|---|---|---|
| `bond` | string | MAS's short name for the bond: SB, then the month and year it's issued. |
| `issue_code` | string | MAS's issue code, the code you apply for at a bank or ATM. |
| `announced` | date | The day MAS announced the bond's interest rates. |
| `last_day_to_apply` | date | The last day to apply. |
| `allotment_date` | date | The day MAS works out who gets how much. |
| `issue_date` | date | The day the bond is issued and interest starts. |
| `maturity_date` | date | The day it pays back the amount you put in, ten years after issue. |
| `year1_interest_pct` | number | The interest the bond pays in year 1 after issue. Unit: percent a year. |
| `year2_interest_pct` | number | The interest the bond pays in year 2 after issue. Unit: percent a year. |
| `year3_interest_pct` | number | The interest the bond pays in year 3 after issue. Unit: percent a year. |
| `year4_interest_pct` | number | The interest the bond pays in year 4 after issue. Unit: percent a year. |
| `year5_interest_pct` | number | The interest the bond pays in year 5 after issue. Unit: percent a year. |
| `year6_interest_pct` | number | The interest the bond pays in year 6 after issue. Unit: percent a year. |
| `year7_interest_pct` | number | The interest the bond pays in year 7 after issue. Unit: percent a year. |
| `year8_interest_pct` | number | The interest the bond pays in year 8 after issue. Unit: percent a year. |
| `year9_interest_pct` | number | The interest the bond pays in year 9 after issue. Unit: percent a year. |
| `year10_interest_pct` | number | The interest the bond pays in year 10 after issue. Unit: percent a year. |
| `avg_return_if_held_1y_pct` | number | The average return a year if you hold the bond for 1 year and then cash it in. Unit: percent a year. |
| `avg_return_if_held_2y_pct` | number | The average return a year if you hold the bond for 2 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_3y_pct` | number | The average return a year if you hold the bond for 3 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_4y_pct` | number | The average return a year if you hold the bond for 4 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_5y_pct` | number | The average return a year if you hold the bond for 5 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_6y_pct` | number | The average return a year if you hold the bond for 6 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_7y_pct` | number | The average return a year if you hold the bond for 7 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_8y_pct` | number | The average return a year if you hold the bond for 8 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_9y_pct` | number | The average return a year if you hold the bond for 9 years and then cash it in. Unit: percent a year. |
| `avg_return_if_held_10y_pct` | number | The average return a year if you hold the bond for 10 years and then cash it in. Unit: percent a year. |
| `amount_offered_sgd_m` | number | How much MAS offered in this bond. Unit: S$ million. |
| `applied_within_limits_sgd_m` | number | How much people applied for, counting only what fits within each person's limit. Unit: S$ million. Empty when not out yet. |
| `allotted_sgd_m` | number | How much was given out. Unit: S$ million. Empty when not out yet. |
| `full_allotment_up_to_sgd` | integer | When more was asked for than offered: everyone got up to this amount in full. Unit: S$. Empty when it does not apply to that row or not out yet. |
| `random_extra_500_pct` | number | When more was asked for than offered: the share of applicants above that amount who got one more S$500, picked at random. Unit: percent of applicants above that amount. Empty when it does not apply to that row or not out yet. |
| `source` | string | Where the row comes from. |

## Where the numbers come from

- [Monetary Authority of Singapore (MAS)](https://www.mas.gov.sg/statistics), under the [MAS Terms of Use of Datasets](https://www.mas.gov.sg/terms-of-use)

How each figure is read and checked: [numbers.sg/rates/singapore-savings-bonds/#method](https://numbers.sg/rates/singapore-savings-bonds/#method). Every fix is listed on [numbers.sg/corrections](https://numbers.sg/corrections/). Changes as a feed: [`https://numbers.sg/api/v1/ssb-issues/changes.atom`](https://numbers.sg/api/v1/ssb-issues/changes.atom).

## Corrections

Each mistake found in this dataset or on its page, newest first. The same list is on [numbers.sg/corrections](https://numbers.sg/corrections/).

- **8 Nov 2026:** The Savings Bond page said the first payment “is on Jun 2027” and the bond “matures on” a month: these are months, not dates, so both now read “in”. The payment months themselves were right.

Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml) with where you read the right one, or email hello@numbers.sg.

## Credit and citation

Free to use, in paid products too, under [CC BY 4.0](https://numbers.sg/data/licence/). Credit:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/rates/singapore-savings-bonds/), CC BY 4.0

The publishers ask for this notice wherever you use their figures. Copy it as it is:

> Contains information from Singapore Savings Bonds issuance calendar, results and interest rates, and SGS benchmark yields accessed on 2026-11-27 from Monetary Authority of Singapore which is made available under the terms of the Monetary Authority of Singapore’s Terms of Use of Datasets (https://www.mas.gov.sg/terms-of-use)

To cite it:

```
Numbers.sg (2026). Singapore Savings Bonds: rates and results [Data set]. https://numbers.sg/rates/singapore-savings-bonds/
Part of: Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

```bibtex
@misc{numberssg_ssb_issues,
  author = {{Numbers.sg}},
  title = {{Singapore Savings Bonds: rates and results}},
  year = {2026},
  howpublished = {\url{https://numbers.sg/rates/singapore-savings-bonds/}},
  note = {Rows last changed 2026-11-27; CC BY 4.0; archived in https://doi.org/10.5281/zenodo.24576628}
}
```

For a copy that never changes, cite the API's dated copy: `https://numbers.sg/api/v1/ssb-issues/as-of/YYYY-MM-DD`.
