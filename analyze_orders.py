"""Analyze a synthetic exam-prep course order dataset.

This is a learning example, not an official Adda247 analysis.
Run from the repository root: python src/analyze_orders.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "student_orders.csv"

def main():
    df = pd.read_csv(DATA_PATH)
    print("STUDENT COURSE REVENUE ANALYSIS — SYNTHETIC DATA")
    print(f"Rows: {len(df)} | Unique order IDs: {df['order_id'].nunique()}")

    # Basic data-quality checks
    print("\nMissing values by column:")
    print(df.isna().sum().to_string())
    print(f"Duplicate order IDs: {df['order_id'].duplicated().sum()}")

    print("\nOrder status mix:")
    print(df["status"].value_counts().to_string())

    paid = df[df["status"].eq("SUCCESS")].copy()
    total_revenue = paid["amount_inr"].sum()
    print(f"\nSuccessful paid orders: {len(paid)}")
    print(f"Successful paid revenue: ₹{total_revenue:,.0f}")
    print(f"Average successful order value: ₹{paid['amount_inr'].mean():,.2f}")

    by_exam = (
        paid.groupby("exam_category", as_index=False)
        .agg(successful_orders=("order_id", "count"),
             revenue_inr=("amount_inr", "sum"))
        .sort_values("revenue_inr", ascending=False)
    )
    print("\nRevenue by exam category:")
    print(by_exam.to_string(index=False))

    by_channel = (
        paid.groupby("acquisition_channel", as_index=False)
        .agg(successful_orders=("order_id", "count"),
             revenue_inr=("amount_inr", "sum"))
        .sort_values("revenue_inr", ascending=False)
    )
    print("\nRevenue by acquisition channel:")
    print(by_channel.to_string(index=False))

    print("\nInterpretation caution:")
    print("- These rows are synthetic and too small for business decisions.")
    print("- Revenue by channel is not ROI; no spend or traffic data is provided.")
    print("- Correlation or group differences do not prove that a channel caused purchases.")

if __name__ == "__main__":
    main()
