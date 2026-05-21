import matplotlib.pyplot as plt
from tax_analysis import load_merged_data, get_latest_tax_ranking, get_latest_tax_amount_ranking

def plot_tax_share_latest(fuel_type="euro95", n=10, save_file=None):
    df = load_merged_data()
    latest_df, latest_date = get_latest_tax_ranking(df, fuel_type=fuel_type)

    top_n = latest_df.head(n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_n["country_name"], top_n["tax_share"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Tax share")
    plt.title(f"Highest tax shares for {fuel_type} on {latest_date.date()}")
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()

def plot_tax_amount_latest(fuel_type="euro95", n=10, save_file=None):
    df = load_merged_data()
    latest_df, latest_date = get_latest_tax_amount_ranking(df, fuel_type=fuel_type)

    top_n = latest_df.head(n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_n["country_name"], top_n["tax_amount"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Tax amount per 1000 liters")
    plt.title(f"Highest tax amounts for {fuel_type} on {latest_date.date()}")
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()

def plot_with_vs_without_tax(fuel_type="euro95", countries=None, save_file=None):
    if countries is None:
        countries = ["Czech Republic", "Poland", "Germany", "Austria", "Slovakia"]

    df = load_merged_data()
    latest_date = df["Date"].max()

    latest_df = df[
        (df["Date"] == latest_date) &
        (df["fuel_type"] == fuel_type) &
        (df["country_name"].isin(countries))
    ].copy()

    latest_df = latest_df.set_index("country_name").loc[countries].reset_index()

    x = range(len(latest_df))
    width = 0.4

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], latest_df["price_wo_tax"], width=width, label="Without tax")
    plt.bar([i + width/2 for i in x], latest_df["price_with_tax"], width=width, label="With tax")

    plt.xticks(list(x), latest_df["country_name"], rotation=45, ha="right")
    plt.ylabel("Price per 1000 liters")
    plt.title(f"With-tax vs without-tax prices for {fuel_type} on {latest_date.date()}")
    plt.legend()
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()