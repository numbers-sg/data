# Singapore rates and prices: open data from Numbers.sg

[![Data checks](https://github.com/numbers-sg/data/actions/workflows/validate.yml/badge.svg)](https://github.com/numbers-sg/data/actions/workflows/validate.yml) [![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC_BY_4.0-13233A)](LICENSE) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24576628.svg)](https://doi.org/10.5281/zenodo.24576628) ![28 datasets](https://img.shields.io/badge/datasets-28-13233A) ![91,818 rows](https://img.shields.io/badge/rows-91,818-13233A) ![Rows last changed 2026-11-28](https://img.shields.io/badge/rows_last_changed-2026--11--28-13233A)

28 datasets of Singapore interest rates and government bonds (SORA, T-bills, Singapore Savings Bonds), COE bidding results, CPF figures, income tax rates, inflation and exchange rates for the Singapore dollar, as CSV and JSON. Each is read from the agency or bank that publishes it, checked against the page it appears on, and free to use under [CC BY 4.0](LICENSE).

91,818 rows in all, the oldest from Jul 1955 (CPF Ordinary Wage ceiling, since 1955). Rows last changed here on 28 Nov 2026.

This repository is a copy of the [Numbers.sg data API](https://numbers.sg/developers/), refreshed every night at 00:20 Singapore time and committed only when the rows change. For the freshest numbers, use the API: it is free and needs no key, and every answer says when we last read the source.

## Who checks these numbers

Numbers.sg is edited by [Jeremiah Say](https://numbers.sg/about/jeremiah-say/) and published by [Numbers Publishing Pte. Ltd.](https://numbers.sg/company/), a Singapore company. Every figure here goes through the same checks as the page it comes from:

1. **Read from the source.** A scheduled job reads each figure from the agency or bank that publishes it. Figures that change rarely are kept by hand and re-read on a booked date, listed on the [update schedule](https://numbers.sg/update-schedule/).
2. **Matched every night.** Before the nightly copy is saved, a job compares each dataset with the table on its own page, cell by cell.
3. **Checked again here.** Every commit to this repository runs [`scripts/validate.py`](scripts/validate.py): headers, row counts, types, empty values and duplicate rows. The nightly update won't commit a copy that fails it.
4. **Corrected in the open.** Each mistake is listed with its date and what changed, in the dataset's README and on [numbers.sg/corrections](https://numbers.sg/corrections/).

How each dataset is read is set out on its page, under "How we get these numbers", and the overall method at [numbers.sg/how-we-get-our-numbers](https://numbers.sg/how-we-get-our-numbers/). Numbers.sg is independent: none of it is part of, endorsed by or paid by the Singapore Government or any of its agencies, it is not part of any bank, and no one pays for a figure, a ranking or a place on a page.

## Recent corrections

- **26 Nov 2026**, [Singapore dollar to Chinese yuan, since 1993 (daily from 2003)](datasets/fx-sgd-cny/#corrections): SGD to CNY: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them.
- **26 Nov 2026**, [Singapore dollar to Indian rupee, daily since 2006](datasets/fx-sgd-inr/#corrections): SGD to INR: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them.
- **26 Nov 2026**, [Singapore dollar to Japanese yen, since 1988 (daily from 2003)](datasets/fx-sgd-jpy/#corrections): SGD to JPY: the CSV’s note said it held SingStat’s monthly averages for the years before the daily record, but the file had none of them.
- **26 Nov 2026**, [Singapore dollar to Korean won, daily since 1981](datasets/fx-sgd-krw/#corrections): SGD to KRW: the history before 2003 had rates for 12 and 15 December 1997, at the height of the Asian financial crisis.
- **8 Nov 2026**, [Singapore Savings Bonds: rates and results](datasets/ssb-issues/#corrections): The Savings Bond page said the first payment “is on Jun 2027” and the bond “matures on” a month: these are months, not dates, so both now read “in”.

Every correction: [numbers.sg/corrections](https://numbers.sg/corrections/). Found a wrong number? [Report it](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml).

## Datasets

### Interest rates and government bonds

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [Singapore Savings Bonds: rates and results](datasets/ssb-issues/) | `ssb-issues` | 135 | 1 Oct 2015 to 1 Dec 2026 | 27 Nov 2026 |
| [Singapore T-bill auction results](datasets/tbill-auctions/) | `tbill-auctions` | 343 | 25 May 1987 to 19 Nov 2026 | 27 Nov 2026 |
| [SORA and Compounded SORA, daily](datasets/sora/) | `sora` | 5,373 | 1 Jul 2005 to 26 Nov 2026 | 27 Nov 2026 |

### Cars

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [COE bidding results, every round since 2010](datasets/coe-results/) | `coe-results` | 2,000 | Jan 2010 to Nov 2026 | 27 Nov 2026 |

### CPF

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [CPF Ordinary Wage ceiling, since 1955](datasets/cpf-wage-ceilings/) | `cpf-wage-ceilings` | 46 | Jul 1955 to Jan 2026 | 27 Nov 2026 |

### Tax

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [Singapore resident income tax rates](datasets/income-tax-rates/) | `income-tax-rates` | 13 | Today’s figures (not a time series) | 27 Nov 2026 |

### Prices

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [Singapore inflation: CPI and MAS Core, monthly since 1961](datasets/inflation/) | `inflation` | 790 | Jan 1961 to Oct 2026 | 27 Nov 2026 |

### Exchange rates

| Dataset | Id | Rows | Covers | Rows last changed |
|---|---|---:|---|---|
| [Malaysian banks' counter rates for the Singapore dollar, daily since 2021](datasets/fx-sgd-myr-bank-counter/) | `fx-sgd-myr-bank-counter` | 1,445 | 4 Jan 2021 to 27 Nov 2026 | 27 Nov 2026 |
| [Singapore dollar to Chinese yuan, monthly averages since 1993](datasets/fx-sgd-cny-monthly/) | `fx-sgd-cny-monthly` | 401 | Jun 1993 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Chinese yuan, since 1993 (daily from 2003)](datasets/fx-sgd-cny/) | `fx-sgd-cny` | 6,502 | 4 Jun 1993 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to euro, daily since 1999](datasets/fx-sgd-eur/) | `fx-sgd-eur` | 7,025 | 4 Jan 1999 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to euro, monthly averages since 1999](datasets/fx-sgd-eur-monthly/) | `fx-sgd-eur-monthly` | 334 | Jan 1999 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Indian rupee, daily since 2006](datasets/fx-sgd-inr/) | `fx-sgd-inr` | 5,247 | 3 Jan 2006 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Indian rupee, monthly averages since 2006](datasets/fx-sgd-inr-monthly/) | `fx-sgd-inr-monthly` | 250 | Jan 2006 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Indonesian rupiah, daily since 1999](datasets/fx-sgd-idr/) | `fx-sgd-idr` | 7,025 | 4 Jan 1999 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Indonesian rupiah, monthly averages since 2003](datasets/fx-sgd-idr-monthly/) | `fx-sgd-idr-monthly` | 286 | Jan 2003 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Japanese yen, monthly averages since 1988](datasets/fx-sgd-jpy-monthly/) | `fx-sgd-jpy-monthly` | 466 | Jan 1988 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Japanese yen, since 1988 (daily from 2003)](datasets/fx-sgd-jpy/) | `fx-sgd-jpy` | 6,783 | 8 Jan 1988 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Korean won, daily since 1981](datasets/fx-sgd-krw/) | `fx-sgd-krw` | 11,409 | 13 Apr 1981 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Malaysian ringgit, daily since 1999](datasets/fx-sgd-myr/) | `fx-sgd-myr` | 7,145 | 4 Jan 1999 to 26 Nov 2026 | 27 Nov 2026 |
| [Singapore dollar to Malaysian ringgit, monthly averages since 1988](datasets/fx-sgd-myr-monthly/) | `fx-sgd-myr-monthly` | 466 | Jan 1988 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Philippine peso, daily since 1999](datasets/fx-sgd-php/) | `fx-sgd-php` | 7,025 | 4 Jan 1999 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Philippine peso, monthly averages since 2003](datasets/fx-sgd-php-monthly/) | `fx-sgd-php-monthly` | 286 | Jan 2003 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to South Korean won, monthly averages since 2003](datasets/fx-sgd-krw-monthly/) | `fx-sgd-krw-monthly` | 286 | Jan 2003 to Oct 2026 | 27 Nov 2026 |
| [Singapore dollar to Thai baht, daily since 1981](datasets/fx-sgd-thb/) | `fx-sgd-thb` | 11,443 | 2 Jan 1981 to 27 Nov 2026 | 28 Nov 2026 |
| [Singapore dollar to Thai baht, monthly averages since 2003](datasets/fx-sgd-thb-monthly/) | `fx-sgd-thb-monthly` | 286 | Jan 2003 to Oct 2026 | 27 Nov 2026 |
| [US dollar to Singapore dollar, daily since 1981](datasets/fx-usd-sgd/) | `fx-usd-sgd` | 8,542 | 2 Jan 1981 to 27 Nov 2026 | 28 Nov 2026 |
| [US dollar to Singapore dollar, monthly averages since 1988](datasets/fx-usd-sgd-monthly/) | `fx-usd-sgd-monthly` | 466 | Jan 1988 to Oct 2026 | 27 Nov 2026 |

Each folder has the CSV, a JSON copy with the field list and sources, and a README with every field's meaning, the sources and their terms, and how to cite it.

## Quick start

```python
import pandas as pd
sora = pd.read_csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv")
```

```r
sora <- read.csv("https://raw.githubusercontent.com/numbers-sg/data/main/datasets/sora/sora.csv")
```

```bash
curl -s https://numbers.sg/api/v1/sora            # the newest rows, as JSON
curl -s https://numbers.sg/api/v1/sora.csv        # every row, as CSV
```

Google Sheets: `=IMPORTDATA("https://numbers.sg/api/v1/coe-results.csv")` gives a table that refreshes itself.

[`index.json`](index.json) lists every dataset with its rows, dates and hash. [`datapackage.json`](datapackage.json) describes the CSVs in the [Frictionless](https://frictionlessdata.io/) standard, so `frictionless` and pandas read them with their types.

## Freshness and changes

- The API reads each source on its own schedule, as often as every 10 minutes on COE results days. The [update schedule](https://numbers.sg/update-schedule/) lists each one.
- Every API answer says when we last read the source (`meta.checked_at`) and whether that read is late (`meta.stale`).
- Follow every change in a feed reader: [`https://numbers.sg/api/v1/changes.atom`](https://numbers.sg/api/v1/changes.atom) (JSON Feed: [`changes.json`](https://numbers.sg/api/v1/changes.json)).
- Mistakes are fixed in the open, with the date and what changed, on [numbers.sg/corrections](https://numbers.sg/corrections/).

## Licence and credit

Free to use, in apps, research, articles and paid products, under [CC BY 4.0](LICENSE). Credit Numbers.sg and the publisher, for example:

> Source: Monetary Authority of Singapore, compiled by Numbers.sg (numbers.sg/rates/sora/), CC BY 4.0

Each dataset's README has its exact credit line, and any notice its publisher asks you to carry. What the licence covers and what it doesn't is set out in plain words at [numbers.sg/data/licence](https://numbers.sg/data/licence/).

## Citing

**DOI: [10.5281/zenodo.24576628](https://doi.org/10.5281/zenodo.24576628)**. Each January a dated snapshot of this repository is archived on Zenodo; this DOI always resolves to the newest one, and each snapshot has its own DOI for a copy that never changes.

```
Say, J. (2026). Singapore Interest Rates, COE Prices, CPF, Income Tax, Inflation and SGD Exchange Rates (Numbers.sg Open Data) [Data set]. Numbers.sg. https://doi.org/10.5281/zenodo.24576628
```

GitHub's "Cite this repository" button uses [`CITATION.cff`](CITATION.cff). Each dataset's README has its own citation and BibTeX entry. To cite numbers as they stood on a given day, use the API's dated copies: `https://numbers.sg/api/v1/{id}/as-of/YYYY-MM-DD`, saved every night since 26 Nov 2026 and never changed afterwards.

## Not in this repository

These datasets rest on at least one source whose terms grant no reuse beyond personal use. We publish their figures as facts on Numbers.sg and in the API, but we don't redistribute the whole series here. Read each source's terms before republishing:

- Additional Buyer's Stamp Duty (ABSD) rates, since 2011: [`https://numbers.sg/api/v1/absd-rates`](https://numbers.sg/api/v1/absd-rates)
- Buyer's Stamp Duty (BSD) rates, since 2013: [`https://numbers.sg/api/v1/bsd-rates`](https://numbers.sg/api/v1/bsd-rates)
- CPF contribution rate tables, this year and next: [`https://numbers.sg/api/v1/cpf-contribution-tables`](https://numbers.sg/api/v1/cpf-contribution-tables)
- CPF contribution rates by age, since 1955: [`https://numbers.sg/api/v1/cpf-contribution-rates`](https://numbers.sg/api/v1/cpf-contribution-rates)
- CPF interest rates, since 1955: [`https://numbers.sg/api/v1/cpf-interest-rates`](https://numbers.sg/api/v1/cpf-interest-rates)
- CPF retirement sums (BRS, FRS, ERS), since 2003: [`https://numbers.sg/api/v1/cpf-retirement-sums`](https://numbers.sg/api/v1/cpf-retirement-sums)
- Every ABSD change, with the government's reasons: [`https://numbers.sg/api/v1/absd-changes`](https://numbers.sg/api/v1/absd-changes)
- Singapore household electricity tariff, quarterly since 2005: [`https://numbers.sg/api/v1/electricity-tariff`](https://numbers.sg/api/v1/electricity-tariff)

## About

[Numbers.sg](https://numbers.sg/) tracks Singapore rates, prices and rules, each read from its official source. It is independent: none of it is part of, endorsed by or paid by the Singapore Government or any of its agencies, it is not part of any bank, and no one pays for a figure, a ranking or a place on a page. Something that looks wrong: [report a wrong number](https://github.com/numbers-sg/data/issues/new?template=wrong-number.yml). A dataset you'd like: [ask for it](https://github.com/numbers-sg/data/issues/new?template=dataset-request.yml). Or write to hello@numbers.sg.
