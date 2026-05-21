import pandas as pd
from analysis import add_country_names, keep_eu_countries_only

def load_merged_data(file="prices_merged.csv"):
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"])
    df = add_country_names(df)
    df = keep_eu_countries_only(df)
    return df

def get_latest_tax_ranking(df, fuel_type="euro95"):
    latest_date = df["Date"].max()

    latest_df = df[
        (df["Date"] == latest_date) &
        (df["fuel_type"] == fuel_type)
    ].copy()

    latest_df = latest_df.dropna(subset=["tax_share"]).copy()
    latest_df = latest_df.sort_values("tax_share", ascending=False).reset_index(drop=True)

    return latest_df, latest_date

def get_latest_tax_amount_ranking(df, fuel_type="euro95"):
    latest_date = df["Date"].max()

    latest_df = df[
        (df["Date"] == latest_date) &
        (df["fuel_type"] == fuel_type)
    ].copy()

    latest_df = latest_df.dropna(subset=["tax_amount"]).copy()
    latest_df = latest_df.sort_values("tax_amount", ascending=False).reset_index(drop=True)

    return latest_df, latest_date