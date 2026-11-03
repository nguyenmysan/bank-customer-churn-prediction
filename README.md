<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Arial&weight=700&size=26&duration=3000&pause=1000&color=0876C9&center=true&vCenter=true&width=650&lines=Bank+Customer+Churn+Prediction" alt="Bank Customer Churn Prediction" />
</div>
### A Hypothetical Case Study for JPMorganChase

**Author:** Nguyen My San  

## 1. Project Overview

This project explores bank customer churn using exploratory data analysis (EDA) and supervised machine learning.

The goal is to identify factors associated with customer churn and develop a Logistic Regression model to support customer retention decisions.

**Research Question:** How accurately can Logistic Regression predict customer churn using demographic, financial, and account-related characteristics?

**Disclaimer:** This is an independent academic project using synthetic Kaggle data. JPMorganChase is a hypothetical stakeholder and did not provide the data.

## 2. Dataset

**Source:** [Kaggle Playground Series S4E1](https://www.kaggle.com/competitions/playground-series-s4e1/data)

- Training data: 165,034 rows × 14 columns
- Target: `Exited` (0 = Stayed, 1 = Exited)
- Features: Age, CreditScore, Geography, Balance, Tenure, NumOfProducts, IsActiveMember, and others
- Dataset type: Synthetic banking data

Raw CSV files are not included in this repository.

## 3. Initial EDA Findings

| Analysis | Key Finding |
|---|---|
| Overall churn | 21.2% exited |
| Customer activity | Inactive: 29.7%; Active: 12.5% |
| Number of products | 1 product: 34.7%; 2 products: 6.0% |
| Age groups | Ages 51–60: 60.9% churn |

These are descriptive findings, not causal conclusions.

## 4. Project Structure

```text
bank-customer-churn-prediction/
├── data/                   # Download train.csv separately
├── src/
│   └── bank_churn_analysis.py
├── reports/                # Generated EDA outputs
├── docs/                   # P1 report PDF
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. How to Run the Project (macOS and Windows)

### Step 1: Clone the Repository

```bash
git clone https://github.com/nguyenmysan/bank-customer-churn-prediction.git
cd bank-customer-churn-prediction
```

### Step 2: Create and Activate a Virtual Environment

**macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Download the Dataset

1. Download the competition files from [Kaggle](https://www.kaggle.com/competitions/playground-series-s4e1/data).
2. Extract the downloaded ZIP.
3. Place **only `train.csv`** inside the `data/` folder.

Required path: `data/train.csv`

### Step 5: Run the Analysis

**macOS and Windows:**

```bash
python src/bank_churn_analysis.py
```

### Step 6: Verify Results

The script should generate four EDA visualizations in `reports/`:

- Overall churn distribution
- Churn by customer activity
- Churn by number of products
- Churn by age group

Expected results: **165,034 observations**, **34,921 exited**, and **21.2% overall churn**.

## 6. Modeling Plan

- Investigate repeated CustomerId values and potential data leakage.
- Split data into training, validation, and holdout sets.
- Train a majority-class baseline and Logistic Regression.
- Evaluate Precision, Recall, F1-score, ROC-AUC, and confusion matrix.

**Current status:** P1 EDA completed; model training is planned for the next phase.

## 7. P1 Submission & Peer Validation

The P1 PDF report will be stored in `docs/`.

Peer validators should clone the repository, follow the setup instructions independently, run the analysis, and verify the expected results.

The Assignment Validation document is submitted separately according to course instructions.

## References

- [Kaggle – Bank Churn Dataset](https://www.kaggle.com/competitions/playground-series-s4e1/data)

c
