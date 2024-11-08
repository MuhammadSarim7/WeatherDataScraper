import requests
from bs4 import BeautifulSoup


def fetch_weather_data(city_name, weather_url="https://www.accuweather.com/en/search-locations?query="):
    search_url = f"{weather_url}{city_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        city_url = soup.find("a", class_="result-city-link")["href"]
        city_weather_url = f"https://www.accuweather.com{city_url}"
        city_response = requests.get(city_weather_url, headers=headers)
        city_soup = BeautifulSoup(city_response.content, "html.parser")
        temperature = city_soup.find("span", class_="temp").text.strip()
        condition = city_soup.find("span", class_="phrase").text.strip()
    except AttributeError:
        temperature, condition = "N/A", "N/A"

    return {"city": city_name, "temperature": temperature, "condition": condition}


def get_multiple_city_weather(cities, weather_url="https://www.accuweather.com/en/search-locations?query="):
    weather_data = []
    for city in cities:
        weather_data.append(fetch_weather_data(city, weather_url))
    return weather_data
