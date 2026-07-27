import pandas as pd

# Read Fund Master Dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Mutual Fund Schemes:")
print(fund_master.shape[0])

print("\nTotal Columns:")
print(fund_master.shape[1])

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

print("\nMissing Values:")
print(fund_master.isnull().sum())