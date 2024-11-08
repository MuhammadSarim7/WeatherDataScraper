import streamlit as st
import pandas as pd
from weather_scraper import get_multiple_city_weather

st.title("Weather Dashboard")
st.header("Weather Data for Multiple Cities")

cities_input = st.text_input(
    "Enter cities separated by commas", "Faisalabad, Lahore, Islamabad"
)

cities = [city.strip() for city in cities_input.split(",")]

weather_data = get_multiple_city_weather(cities)

weather_df = pd.DataFrame(weather_data)

city_filter = st.text_input("Search for a city", "")
if city_filter:
    weather_df = weather_df[weather_df["city"].str.contains(
        city_filter, case=False)]

sort_by_temp = st.checkbox("Sort by Temperature")
if sort_by_temp:
    weather_df["temperature"] = weather_df["temperature"].apply(
        lambda x: int(x.split()[0]) if x != "N/A" else 0
    )
    weather_df = weather_df.sort_values(by="temperature", ascending=False)

st.dataframe(weather_df)
