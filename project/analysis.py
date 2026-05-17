import pandas as pd

def load_data(file="prices_with_taxes_long.csv"):
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def add_country_names(df):
    country_map = {
        "AT": "Austria",
        "BE": "Belgium",
        "BG": "Bulgaria",
        "CY": "Cyprus",
        "CZ": "Czech Republic",
        "DE": "Germany",
        "DK": "Denmark",
        "EE": "Estonia",
        "ES": "Spain",
        "EU": "European Union",
        "EUR": "Euro Area",
        "FI": "Finland",
        "FR": "France",
        "GR": "Greece",
        "HR": "Croatia",
        "HU": "Hungary",
        "IE": "Ireland",
        "IT": "Italy",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "LV": "Latvia",
        "MT": "Malta",
        "NL": "Netherlands",
        "PL": "Poland",
        "PT": "Portugal",
        "RO": "Romania",
        "SE": "Sweden",
        "SI": "Slovenia",
        "SK": "Slovakia",
        "UK": "United Kingdom"
    }

    df = df.copy()
    df["country_name"] = df["country"].map(country_map)
    return df

def keep_eu_countries_only(df):
    return df[~df["country"].isin(["EU", "EUR", "UK"])].copy()

def get_latest_ranking(df, fuel_type="euro95", tank_size=50):
    latest_date = df["Date"].max()
    latest_df = df[df["Date"] == latest_date].copy()

    fuel_df = latest_df[latest_df["fuel_type"] == fuel_type].copy()
    fuel_df["tank_cost"] = fuel_df["price_per_1000l"] / 1000 * tank_size
    fuel_df = fuel_df.sort_values("tank_cost").reset_index(drop=True)

    return fuel_df, latest_date