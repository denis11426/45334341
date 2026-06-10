import plotly.express as px
import streamlit as st


def show_fuel_price_map(fuel_df, fuel_type, latest_date):

    map_df = fuel_df.copy()

    map_df["price_per_1000l"] = map_df["price_per_1000l"].round(2)
    map_df["tank_cost"] = map_df["tank_cost"].round(2)

    map_df["country_name_plotly"] = map_df["country_name"].replace({
        "Czech Republic": "Czechia"
    })

    fig_map = px.choropleth(
        map_df,
        locations="country_name_plotly",
        locationmode="country names",
        color="price_per_1000l",
        hover_name="country_name",
        hover_data={
            "country_name_plotly": False,
            "country_name": False,
            "price_per_1000l": ":.2f",
            "tank_cost": ":.2f"
        },
        scope="europe",
        color_continuous_scale="Reds"
    )

    fig_map.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_map.update_layout(
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        coloraxis_colorbar_title="Price per 1000L"
    )

    st.plotly_chart(fig_map, use_container_width=True)