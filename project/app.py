import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analysis import load_data, add_country_names, keep_eu_countries_only, get_latest_ranking
from tax_analysis import load_merged_data


st.set_page_config(page_title="EU Fuel Price Dashboard", layout="wide")

st.title("EU Fuel Price Dashboard")
st.write("Interactive dashboard for comparing fuel prices across EU countries")

# Sidebar controls
fuel_type = st.sidebar.selectbox("Choose fuel type", ["euro95", "diesel"])
tank_size = st.sidebar.slider("Choose tank size (liters)", 30, 80, 50)

default_countries = ["Czech Republic", "Poland", "Germany", "Austria", "Slovakia"]
selected_countries = st.sidebar.multiselect(
    "Choose countries for comparison",
    options=[
        "Austria", "Belgium", "Bulgaria", "Cyprus", "Czech Republic", "Germany",
        "Denmark", "Estonia", "Spain", "Finland", "France", "Greece", "Croatia",
        "Hungary", "Ireland", "Italy", "Lithuania", "Luxembourg", "Latvia",
        "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Sweden",
        "Slovenia", "Slovakia"
    ],
    default=default_countries
)

# Load price data
df = load_data()
df = add_country_names(df)
df = keep_eu_countries_only(df)

fuel_df, latest_date = get_latest_ranking(df, fuel_type=fuel_type, tank_size=tank_size)

st.subheader(f"Top 10 cheapest countries for {fuel_type} on {latest_date.date()}")
st.dataframe(
    fuel_df[["country_name", "price_per_1000l", "tank_cost"]].head(10).reset_index(drop=True)
)

fig1, ax1 = plt.subplots(figsize=(10, 5))
top10 = fuel_df.head(10)
ax1.bar(top10["country_name"], top10["tank_cost"])
ax1.set_ylabel(f"Cost of {tank_size}L tank in euros")
ax1.set_title(f"Top 10 cheapest countries for {fuel_type}")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig1)

st.subheader(f"Cheapest vs most expensive countries for {fuel_type}")
cheapest = fuel_df.head(5)
most_expensive = fuel_df.tail(5)
combined = pd.concat([cheapest, most_expensive], ignore_index=True)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(combined["country_name"], combined["tank_cost"])
ax2.set_ylabel(f"Cost of {tank_size}L tank in euros")
ax2.set_title(f"Cheapest and most expensive countries for {fuel_type}")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig2)

st.subheader(f"{fuel_type} price trends over time")
trend_df = df[
    (df["fuel_type"] == fuel_type) &
    (df["country_name"].isin(selected_countries))
].copy()

fig3, ax3 = plt.subplots(figsize=(12, 6))
for country in selected_countries:
    country_df = trend_df[trend_df["country_name"] == country].sort_values("Date")
    ax3.plot(country_df["Date"], country_df["price_per_1000l"], label=country)

ax3.set_ylabel("Price per 1000 liters")
ax3.set_title(f"{fuel_type} prices over time")
ax3.legend()
plt.tight_layout()
st.pyplot(fig3)

# Tax comparison
merged = load_merged_data()
merged_latest = merged[
    (merged["Date"] == merged["Date"].max()) &
    (merged["fuel_type"] == fuel_type) &
    (merged["country_name"].isin(selected_countries))
].copy()

if not merged_latest.empty:
    st.subheader(f"With-tax vs without-tax prices for {fuel_type} on {merged['Date'].max().date()}")

    merged_latest = merged_latest.set_index("country_name").loc[selected_countries].reset_index()

    x = range(len(merged_latest))
    width = 0.4

    fig4, ax4 = plt.subplots(figsize=(10, 5))
    ax4.bar([i - width/2 for i in x], merged_latest["price_wo_tax"], width=width, label="Without tax")
    ax4.bar([i + width/2 for i in x], merged_latest["price_with_tax"], width=width, label="With tax")

    ax4.set_xticks(list(x))
    ax4.set_xticklabels(merged_latest["country_name"], rotation=45, ha="right")
    ax4.set_ylabel("Price per 1000 liters")
    ax4.set_title(f"With-tax vs without-tax comparison for {fuel_type}")
    ax4.legend()
    plt.tight_layout()
    st.pyplot(fig4)

    st.subheader("Latest tax comparison table")
    st.dataframe(
        merged_latest[[
            "country_name", "price_wo_tax", "price_with_tax", "tax_amount", "tax_share"
        ]].reset_index(drop=True)
    )