
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

df = pd.read_csv(ROOT / "data" / "train.csv")
sns.set_theme(style="whitegrid")

print("=== DATASET OVERVIEW ===")
print("Shape:", df.shape)
print("Missing values:", df.isna().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# 2. Data quality
quality = pd.DataFrame({
    "column": df.columns,
    "dtype": df.dtypes.astype(str).values,
    "missing_count": df.isna().sum().values,
    "unique_values": df.nunique().values
})
quality.to_csv(REPORTS / "data_quality.csv", index=False)

# 3. Customer churn distribution
counts = df["Exited"].value_counts().reindex([0, 1], fill_value=0)
rates = counts / len(df) * 100

print("\n=== CUSTOMER CHURN ===")
print(pd.DataFrame({"count": counts, "percentage": rates.round(2)}))

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(
    ["Stayed (0)", "Exited (1)"],
    counts.values,
    color=["#72B6A1", "#E99675"]
)

for bar, count, rate in zip(bars, counts, rates):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 1500,
            f"{count:,}\n({rate:.1f}%)", ha="center")

ax.set_title("Customer Churn Distribution")
ax.set_ylabel("Number of Customers")
ax.set_ylim(0, counts.max() * 1.15)
plt.tight_layout()
plt.savefig(REPORTS / "01_churn_distribution.png", dpi=200)
plt.close()

# 4. Churn by customer activity
activity = df.groupby("IsActiveMember")["Exited"].agg(["mean", "size"])
activity["churn_rate_pct"] = activity["mean"] * 100
activity.to_csv(REPORTS / "churn_by_activity.csv")

fig, ax = plt.subplots(figsize=(7, 5))
values = activity.reindex([0, 1])["churn_rate_pct"]
sizes = activity.reindex([0, 1])["size"]
ax.bar(["Inactive", "Active"], values, color="steelblue")

for i, (rate, n) in enumerate(zip(values, sizes)):
    ax.text(i, rate + 1, f"{rate:.1f}%\nn={n:,}", ha="center")

ax.set_title("Churn Rate by Customer Activity")
ax.set_ylabel("Churn Rate (%)")
ax.set_ylim(0, 40)
plt.tight_layout()
plt.savefig(REPORTS / "02_churn_by_activity.png", dpi=200)
plt.close()

# 5. Churn by number of products
products = df.groupby("NumOfProducts")["Exited"].agg(["mean", "size"])
products["churn_rate_pct"] = products["mean"] * 100
products.to_csv(REPORTS / "churn_by_products.csv")

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(products.index.astype(str),
       products["churn_rate_pct"], color="steelblue")

for i, (rate, n) in enumerate(
    zip(products["churn_rate_pct"], products["size"])
):
    ax.text(i, rate + 1, f"{rate:.1f}%\nn={n:,}", ha="center")

ax.set_title("Churn Rate by Number of Products")
ax.set_xlabel("Number of Banking Products")
ax.set_ylabel("Churn Rate (%)")
ax.set_ylim(0, 105)
plt.tight_layout()
plt.savefig(REPORTS / "03_churn_by_products.png", dpi=200)
plt.close()

# 6. Churn by age group
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[float("-inf"), 30, 40, 50, 60, float("inf")],
    labels=["30 or younger", "31-40", "41-50", "51-60", "Over 60"]
)

age = df.groupby("AgeGroup", observed=True)["Exited"].agg(["mean", "size"])
age["churn_rate_pct"] = age["mean"] * 100
age.to_csv(REPORTS / "churn_by_age.csv")

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(age.index.astype(str),
       age["churn_rate_pct"], color="steelblue")

for i, (rate, n) in enumerate(zip(age["churn_rate_pct"], age["size"])):
    ax.text(i, rate + 1, f"{rate:.1f}%\nn={n:,}", ha="center")

ax.set_title("Churn Rate by Age Group")
ax.set_xlabel("Age Group")
ax.set_ylabel("Churn Rate (%)")
ax.set_ylim(0, 75)
plt.tight_layout()
plt.savefig(REPORTS / "04_churn_by_age.png", dpi=200)
plt.close()

print("\nEDA completed successfully!")
print("Charts and CSV summaries saved to:", REPORTS)
