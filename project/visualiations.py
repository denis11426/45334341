import matplotlib.pyplot as plt
from analysis import load_data, add_country_names, keep_eu_countries_only, get_latest_ranking

df = load_data()
df = add_country_names(df)
df = keep_eu_countries_only(df)

fuel_df, latest_date = get_latest_ranking(df, fuel_type="euro95", tank_size=50)
top10 = fuel_df.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top10["country_name"], top10["tank_cost"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("Cost of 50L tank in euros")
plt.title(f"Top 10 cheapest countries for euro95 on {latest_date.date()}")
plt.tight_layout()
plt.savefig("top10_euro95_latest.png", dpi=300, bbox_inches="tight")
plt.show()