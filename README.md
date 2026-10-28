# Student Course Revenue Analysis (Adda247-style case study)

## Important disclosure
This is a **self-directed practice project** using a small, synthetic dataset. It is not an official Adda247 project, does not use Adda247 data, and the findings are not real company results. The dataset and analysis were created for learning and interview practice.

## Business question
How can an exam-preparation platform understand paid course revenue across exam categories and acquisition channels, while separating successful payments from failed, free, and refunded orders?

## What is included
- `data/student_orders.csv` — 40 synthetic order records.
- `sql/revenue_analysis.sql` — SQL queries for revenue, channel/category breakdown, order statuses, and customer ranking.
- `src/analyze_orders.py` — Python/Pandas analysis that prints summary tables and checks data quality.
- `requirements.txt` — Python dependency.
- `INTERVIEW_NOTES.md` — how to explain the project and its limitations.

## Definitions used
- **Gross successful sales**: sum of order amounts where status is `SUCCESS`.
- **Net collected revenue (simplified)**: successful sales minus orders marked `REFUNDED`. In this toy dataset, refunds are recorded as order statuses, so only successful orders are included in the gross calculation and refunded orders are excluded from revenue.
- `FREE`, `FAILED`, and `REFUNDED` are not counted as successful paid orders.
- This dataset has no ad spend or visitor counts, so it cannot support CAC or conversion-rate calculations.

## Run locally
Python 3.10+ recommended.

```bash
pip install -r requirements.txt
python src/analyze_orders.py
```

## Run SQL
Open `sql/revenue_analysis.sql` in SQLite Online (https://sqliteonline.com/) and import `data/student_orders.csv` as a table named `student_orders`, or run it in a local SQLite database after importing the CSV.

## Example questions this project helps answer
1. Which exam categories contribute most successful paid revenue?
2. Which acquisition channels bring in successful paid orders?
3. What share of orders are successful, failed, refunded, or free?
4. Which customers have the highest successful spend in this sample?

## Limitations / next steps
- Small synthetic dataset; results are illustrative only.
- No impressions, clicks, marketing spend, course engagement, or renewal data.
- No causal conclusions can be drawn about channel effectiveness.
- Next step: use a larger real or openly licensed dataset, define event-level funnel metrics, and evaluate experiments before recommending budget shifts.
