import pandas as pd


FILE_NAME = "Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx"


def clean_price_sheet(sheet_name, output_clean, output_fuels):
    print(f"\nCleaning sheet: {sheet_name}")

    df = pd.read_excel(FILE_NAME, sheet_name=sheet_name, skiprows=[1])

    df = df.rename(columns={df.columns[0]: "Date"})
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    df = df.dropna(subset=["Date"]).copy()

    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.reset_index(drop=True)

    print("First rows of cleaned data:")
    print(df.head())
    print("\nFirst 15 column names:")
    print(df.columns.tolist()[:15])

    df.to_csv(output_clean, index=False)
    print(f"Cleaned file saved as {output_clean}")

    selected_cols = ["Date"]

    for col in df.columns:
        col_lower = col.lower()
        if "euro95" in col_lower or "diesel" in col_lower:
            selected_cols.append(col)

    fuel_df = df[selected_cols].copy()

    print("\nFirst rows of fuels-only data:")
    print(fuel_df.head())
    print("\nFirst 20 fuel columns:")
    print(fuel_df.columns.tolist()[:20])

    fuel_df.to_csv(output_fuels, index=False)
    print(f"Filtered file saved as {output_fuels}")


def main():
    xls = pd.ExcelFile(FILE_NAME)
    print("Sheets:", xls.sheet_names)

    clean_price_sheet(
        sheet_name="Prices with taxes",
        output_clean="prices_with_taxes_clean.csv",
        output_fuels="prices_with_taxes_fuels_only.csv"
    )

    clean_price_sheet(
        sheet_name="Prices wo taxes",
        output_clean="prices_wo_taxes_clean.csv",
        output_fuels="prices_wo_taxes_fuels_only.csv"
    )


if __name__ == "__main__":
    main()