import pandas as pd

# Read the Fund Master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Required AMFI codes
required_codes = [
    125497,
    119551,
    120503,
    118632,
    120841
]

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

for code in required_codes:

    if code in fund_master["amfi_code"].values:

        scheme = fund_master.loc[
            fund_master["amfi_code"] == code,
            "scheme_name"
        ].values[0]

        print(f"✅ {code} -> {scheme}")

    else:

        print(f"❌ {code} -> NOT FOUND")