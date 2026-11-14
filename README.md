# How Have U.S. Families Changed?

An interactive guess-first activity about long-run trends in U.S. families. Students make five guesses (how old men were at first marriage in 1890, whether divorce is rising, how many children live with two parents, how many households are one person, and whether births to unmarried women are still rising), then explore seven trends going back as far as 1890. By Gwen Sharp.

**Live site:** https://gsharpokie.github.io/familytrends/

## What it does

- **Five guesses,** each followed by the answer and the student’s guess.
- **Explore the trends:** one chart at a time, chosen from seven buttons. Move across the chart or use the year slider to read exact values. Each chart has a “what to notice” note, a “keep in mind” note about how the numbers were collected, and a table of the numbers.
  - Median age at first marriage, men and women, 1890–2025
  - Who children live with (two parents, mother only, father only, no parent), 1960–2025
  - Married-couple households (1940–2025) and one-person households (1960–2025)
  - Average household size, 1940–2025
  - Births to unmarried women, 1940–2024
  - Marriage and divorce rates, 2000–2024
  - Young adults living with a parent, by age and sex, 1960–2025
- **1960 and now:** a table comparing 1960 with the latest year.
- **The fuller picture:** why the 1950s are a misleading starting point, which trends have leveled off, and which are still moving.
- **Discussion questions.**

The page describes change without calling it better or worse. (For improved-or-worsened indicators, see [Better or Worse?](https://gsharpokie.github.io/better-or-worse/))

## For instructors

To show the charts without guessing, add `#charts` to the link: https://gsharpokie.github.io/familytrends/#charts

## Data

- U.S. Census Bureau, historical tables on families and living arrangements (Current Population Survey Annual Social and Economic Supplement through 2025, released December 2025, plus earlier censuses). https://www.census.gov/data/tables/time-series/demo/families.html
  - Table MS-2: median age at first marriage, 1890–2025.
  - Table CH-1: living arrangements of children under 18, 1960–2025. Percentages are calculated from the counts. “No parent” combines the table’s two “no parents” columns.
  - Table HH-1: married-couple households as a percent of all households. Table HH-4: one-person households as a percent of all households. Table HH-6: average people per household.
  - Table AD-1: young adults 18–24 and 25–34 living at home.
  - Where a year has both an original and a revised row, the revised row is used. For 2007 in CH-1, the row using the newer method of identifying two parents is used.
- National Center for Health Statistics, *Provisional Number of Marriages and Marriage Rate* and *Provisional Number of Divorces and Annulments and Rate: United States, 2000–2024*. https://www.cdc.gov/nchs/data/dvs/marriage-divorce/national-marriage-divorce-rates-00-24.pdf
- National Center for Health Statistics, percent of births to unmarried women:
  - 1940–1999: Ventura and Bachrach, “Nonmarital Childbearing in the United States, 1940–99,” *National Vital Statistics Reports* 48(16), 2000, table 1. https://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf
  - 2000–2010: “Births: Final Data for 2010,” *NVSR* 61(1), table C.
  - 2011–2024: the text of each year’s “Births: Final Data” report (*NVSR* 62(1), 62(9), 64(1), 66(1), 67(1), 68(13), 70(17), 72(1), 74(1), and 75(2)). https://www.cdc.gov/nchs/data/nvsr/nvsr75/nvsr75-02.pdf
- Pew Research Center. 2023. “Public Has Mixed Views on the Modern American Family.” https://www.pewresearch.org/social-trends/2023/09/14/public-has-mixed-views-on-the-modern-american-family/

## Editing and updating

All the numbers are in the block between `DATA:START` and `DATA:END` near the top of the `<script>` section of `index.html`. Each series is a list of `year:value` pairs. The answers, “what to notice” notes, table, and most of “The fuller picture” are calculated from those lists, so they update when the numbers do. The wording of each chart’s notes is in `const TRENDS`.

- **Census series** (released each fall): download `ms2.xls`, `ch1.xls`, `hh1.xls`, `hh4.xls`, `hh6.xls`, and `ad1.xls` from https://www2.census.gov/programs-surveys/demo/tables/families/time-series/ into one folder, run `python3 tools/build_data.py FOLDER`, and paste the output over the Census lines in the data block.
- **Marriage and divorce rates:** add the new year to `MAR_RATE` and `DIV_RATE` from the NCHS file, and update the list of states left out in “About the data.”
- **Births to unmarried women:** add the new year to `NONMAR` from the latest “Births: Final Data” report.

## Turning on the site (one time)

Go to **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the **main** branch and the **/ (root)** folder, and select **Save**. Keep Issues turned on so the “Suggest a correction” link works.

## Author

Created by Gwen Sharp ([@gsharpokie](https://x.com/gsharpokie)).

## License

© 2026 Gwen Sharp. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you may share and adapt it for noncommercial purposes with credit. See [LICENSE](LICENSE). The statistics come from the public sources listed above; this license covers the page’s design, text, and code.
