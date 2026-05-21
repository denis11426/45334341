import matplotlib.pyplot as plt
from analysis import load_data, add_country_names, keep_eu_countries_only, get_latest_ranking


def plot_top10_latest(fuel_type="euro95", tank_size=50, save_file=None):
    df = load_data()
    df = add_country_names(df)
    df = keep_eu_countries_only(df)

    fuel_df, latest_date = get_latest_ranking(df, fuel_type=fuel_type, tank_size=tank_size)
    top10 = fuel_df.head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top10["country_name"], top10["tank_cost"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel(f"Cost of {tank_size}L tank in euros")
    plt.title(f"Top 10 cheapest countries for {fuel_type} on {latest_date.date()}")
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()


def plot_selected_countries_trend(fuel_type="euro95", countries=None, save_file=None):
    if countries is None:
        countries = ["Czech Republic", "Poland", "Germany", "Austria", "Slovakia"]

    df = load_data()
    df = add_country_names(df)
    df = keep_eu_countries_only(df)

    df = df[df["fuel_type"] == fuel_type].copy()
    df = df[df["country_name"].isin(countries)].copy()

    plt.figure(figsize=(12, 6))

    for country in countries:
        country_df = df[df["country_name"] == country].sort_values("Date")
        plt.plot(country_df["Date"], country_df["price_per_1000l"], label=country)

    plt.ylabel("Price per 1000 liters")
    plt.title(f"{fuel_type} prices over time")
    plt.legend()
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()


def plot_cheapest_vs_most_expensive(fuel_type="euro95", tank_size=50, n=5, save_file=None):
    df = load_data()
    df = add_country_names(df)
    df = keep_eu_countries_only(df)

    fuel_df, latest_date = get_latest_ranking(df, fuel_type=fuel_type, tank_size=tank_size)

    cheapest = fuel_df.head(n)
    most_expensive = fuel_df.tail(n)
    combined = cheapest._append(most_expensive)

    plt.figure(figsize=(10, 6))
    plt.bar(combined["country_name"], combined["tank_cost"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel(f"Cost of {tank_size}L tank in euros")
    plt.title(f"Cheapest and most expensive countries for {fuel_type} on {latest_date.date()}")
    plt.tight_layout()

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    plot_top10_latest(fuel_type="euro95", tank_size=50, save_file="top10_euro95_latest.png")
    plot_top10_latest(fuel_type="diesel", tank_size=50, save_file="top10_diesel_latest.png")
    plot_selected_countries_trend(
        fuel_type="euro95",
        countries=["Czech Republic", "Poland", "Germany", "Austria", "Slovakia"],
        save_file="euro95_trend_selected_countries.png"
    )
    plot_cheapest_vs_most_expensive(
        fuel_type="diesel",
        tank_size=50,
        n=5,
        save_file="diesel_cheapest_vs_most_expensive.png"
    )