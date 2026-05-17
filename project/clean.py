import pandas as pd

file = "Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx"

xls = pd.ExcelFile(file)
print("Sheets:", xls.sheet_names)

df = pd.read_excel(file, sheet_name="Prices with taxes", skiprows=[1])

df = df.rename(columns={df.columns[0]: "Date"})
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
df = df.dropna(subset=["Date"]).copy()

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.reset_index(drop=True)

print(df.head())
print(df.columns.tolist()[:15])

df.to_csv("prices_with_taxes_clean.csv", index=False)
print("Cleaned file saved as prices_with_taxes_clean.csv")

selected_cols = ["Date"]

for col in df.columns:
    col_lower = col.lower()
    if "euro95" in col_lower or "diesel" in col_lower:
        selected_cols.append(col)

fuel_df = df[selected_cols].copy()

print(fuel_df.head())
print(fuel_df.columns.tolist()[:20])

fuel_df.to_csv("prices_with_taxes_fuels_only.csv", index=False)
print("Filtered file saved as prices_with_taxes_fuels_only.csv")