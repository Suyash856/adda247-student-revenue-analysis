# Student Course Revenue Analysis

**A self-directed SQL and Python practice case study using synthetic exam-preparation order data.**

> **Data and ownership disclaimer:** This is an independent learning project inspired by common analytics questions in online education. It is not affiliated with Adda247, does not use Adda247's internal data, and does not report actual Adda247 performance. All records are fictional and generated for practice.

## 1. Business question

How can an online exam-preparation platform summarize paid course revenue by exam category and acquisition channel while keeping successful payments separate from failed, free, and refunded orders?

## 2. What this project does

- Checks the dataset for missing values and duplicate order IDs.
- Summarizes order statuses.
- Calculates revenue from orders marked `SUCCESS`.
- Compares successful paid revenue by exam category and acquisition channel.
- Ranks users by successful paid spend using a SQL common table expression (CTE) and window function.

## 3. Repository structure

```text
adda247-student-revenue-analysis/
├── data/
│   └── student_orders.csv
├── sql/
│   └── revenue_analysis.sql
├── src/
│   └── analyze_orders.py
├── INTERVIEW_NOTES.md
├── requirements.txt
└── README.md
```

## 4. Dataset

The CSV contains **40 synthetic order records** for practice. Fields include order ID, user ID, exam category, acquisition channel, order amount, and order status. The sample is intentionally small and should not be treated as representative of a real business.

## 5. Metric definitions

- **Successful paid revenue:** Sum of `amount_inr` for rows where `status = 'SUCCESS'`.
- **Successful paid orders:** Count of rows where `status = 'SUCCESS'`.
- **Average successful order value (AOV):** Successful paid revenue divided by the number of successful paid orders.
- **Order-status mix:** Count of orders in each status (`SUCCESS`, `FAILED`, `FREE`, and `REFUNDED`).

Failed, free, and refunded orders are excluded from the successful paid revenue calculation. This sample does not contain enough payment-event detail to calculate refund timing or reconcile partial refunds, so the revenue metric is a simplified order-level measure—not a full accounting measure of net revenue.

## 6. Run the Python analysis

Python 3.10 or later is recommended.

```bash
pip install -r requirements.txt
python src/analyze_orders.py
```

The script prints basic data-quality checks, the order-status mix, successful paid revenue, average successful order value, and revenue summaries by exam category and acquisition channel.

## 7. Run the SQL queries

The queries are in [`sql/revenue_analysis.sql`](sql/revenue_analysis.sql). Import `data/student_orders.csv` into a SQLite database as a table named `student_orders`, then run the SQL file. You can use a local SQLite client or an online SQLite editor that supports CSV import and window functions.

The SQL includes:

1. Order-status counts.
2. Successful paid revenue by exam category.
3. Successful paid revenue by acquisition channel.
4. Customer revenue ranking using a CTE and `RANK()` window function.
5. Duplicate order-ID checks.
6. Checks for missing user IDs and statuses.

## 8. Example business questions

- Which exam categories have the highest successful paid revenue in this sample?
- Which acquisition channels are associated with the most successful paid revenue?
- What is the distribution of successful, failed, free, and refunded orders?
- Which users have the highest successful paid spend?
- What additional data would be needed before recommending a marketing-budget change?

## 9. Limitations and next steps

- The dataset is small and synthetic; results are illustrative only.
- No impressions, clicks, visitors, marketing spend, course engagement, renewals, or cohort history are included.
- Revenue by channel is **not** the same as conversion rate, customer acquisition cost (CAC), or return on ad spend (ROAS).
- The analysis is descriptive and cannot establish that a channel caused purchases.

A stronger follow-up analysis would use a larger, properly sourced dataset; define a funnel from visit to payment; reconcile refunds; and compare channels using traffic, spend, and conversion data. Any experiment or budget recommendation would need an appropriate test design and sufficient sample size.

## 10. Learning goals

This project is intended to practise basic data validation, SQL aggregation, CTEs, window functions, and pandas-based exploratory analysis. It is a learning exercise, not evidence of production analytics experience or measured business impact.
