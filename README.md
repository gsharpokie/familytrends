# Then and Now: The American Family

An interactive guess-first activity about how U.S. families have changed. For each of nine questions, students see where things stood about 50 years ago, guess where they stand now, and then see the answer from federal statistics or national survey research. By Gwen Sharp.

**Live site:** https://gsharpokie.github.io/familytrends/

## What it does

- **Nine questions:** age at first marriage, married-couple households, living alone, divorce, births to unmarried women, age at first birth, fathers’ time on child care, the four “milestones” of adulthood, and intermarriage.
- **Then and now at a glance:** a summary table with sources.
- **All nine answers** in one place.
- **The fuller picture:** why the starting year matters (the 1950s were unusual), why divorce fell and “gray divorce” didn’t, the plateau in unmarried births, record-low fertility, young adults living at home (and the dorm-counting catch), fathers vs. mothers, changing attitudes, and connections to economics, demography, and history.
- **Discussion questions.**

## For instructors

To show all the answers without guessing, add `#answers` to the link: https://gsharpokie.github.io/familytrends/#answers

## Data

- U.S. Census Bureau. 2025. “Census Bureau Releases New Estimates on America’s Families and Living Arrangements” (CB25-TPS.78, Dec. 2, 2025). https://www.census.gov/newsroom/press-releases/2025/families-and-living-arrangements.html
  - Median age at first marriage: women 21.1 (1975), 28.4 (2025); men 23.5 (1975), 30.8 (2025). Also Table MS-2.
  - Married-couple households: 66% (1975), 47% (2025). Married-couple households with own children under 18: 54% (1975), about 37% (2025).
  - One-person households: 20% (1975), 29% (2025; 39.7 million). Householders 65+: about 1 in 5 (1975), over 1 in 4 (2025).
  - Living in parents’ home, 2025: 58% of ages 18–24, 16% of ages 25–34.
- Hemez, Paul, and Jonathan Vespa. 2025. “Significant Drop in Share of Young Adults Achieving Four Milestones.” U.S. Census Bureau. https://www.census.gov/library/stories/2025/08/milestones-to-adulthood.html — 45% of 25- to 34-year-olds had all four milestones in 1975; less than 25% in 2024; most common 2024 combination (independent and working, not married, no kids) about 28%.
- Vespa, Jonathan. 2017. *The Changing Economics and Demographics of Young Adulthood: 1975–2016*. P20-579. — CPS counts dorm residents as living in parents’ home; women 25–34 who were homemakers: 43% (1975), 14% (2016).
- Pew Research Center. 2025. “8 Facts about Divorce in the United States” (Oct. 16, 2025). — Refined divorce rate 22.6 (1980), 20.5 (2008), 14.4 (2023) per 1,000 married women; ages 50+: 3.9 (1990), 11.0 (2008), 10.3 (2023); one-third of ever-married adults have divorced; 47% of those who married in the 1970s.
- Osterman et al. 2026. “Births: Final Data for 2024.” *NVSR* 75(2). — Unmarried births 39.5% (2024), peak 41.0% (2009); mean age at first birth 27.6; total fertility rate 1,599.5 per 1,000 women; teen birth rate 12.6.
- Curtin, Ventura, and Martinez. 2014. NCHS Data Brief 162. — Unmarried births 10.7% (1970).
- Mathews and Hamilton. 2009. NCHS Data Brief 21. — Mean age at first birth 21.4 (1970).
- Livingston and Parker. 2019. “8 Facts about American Dads.” Pew Research Center. — Fathers’ child care 2.5 hrs/week (1965), 8 (2016); housework 4 → 10; mothers 14 and 18 (2016).
- Livingston and Brown. 2017. *Intermarriage in the U.S. 50 Years After Loving v. Virginia*. Pew Research Center. — 3% (1967), 17% (2015); Asian 29%, Hispanic 27%; non-Black adults opposed to a relative marrying a Black person 63% (1990), 14% (2016).
- NCFMR, Bowling Green State University, FP-26-13 and FP-22-15. — Lowest median ages at first marriage in 1956 (22.5 men, 20.1 women); 1890: 26.1 and 22.0.
- Coontz, Stephanie. 1992. *The Way We Never Were*. Basic Books.

## Editing

All nine questions are in `const Q = [` near the top of the `<script>` section of `index.html`. Each has the “then” statement, the question, the answer (`ans`), the bars (`rows`), and the text shown after the guess (`take`). The summary table builds itself from those. “The fuller picture” is plain text in the page.

**Good update candidates:** Census releases new Families and Living Arrangements tables each fall; NCHS publishes final birth data each year. Fathers’ time (2016) and intermarriage (2015) are the oldest figures; replace them if Pew publishes newer national numbers.

## Turning on the site (one time)

Go to **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the **main** branch and the **/ (root)** folder, and select **Save**. Keep Issues turned on so the “Suggest a correction” link works.

## Author

Created by Gwen Sharp ([@gsharpokie](https://x.com/gsharpokie)).

## License

© 2026 Gwen Sharp. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you may share and adapt it for noncommercial purposes with credit. See [LICENSE](LICENSE). The data belong to their original sources; this license covers the page’s design, text, and code.
