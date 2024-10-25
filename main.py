import requests
import json
import time

API_KEY = '2a27f4c224731b11a791b6444dd3e9bc'  # Replace with your OpenWeatherMap API key
CITY_IDS = ["1273294", "1275339", "1264527", "1277333", "1275004", "1269843"]  # Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def get_weather_data():
    weather_data = []
    for city_id in CITY_IDS:
        try:
            response = requests.get(BASE_URL, params={"id": city_id, "appid": API_KEY})
            data = response.json()

            # Print the full JSON response for debugging
            print(f"Response for city_id {city_id}:\n{json.dumps(data, indent=4)}\n")

            if 'main' in data and 'weather' in data:
                temp = kelvin_to_celsius(data['main'].get('temp', 0))
                feels_like = kelvin_to_celsius(data['main'].get('feels_like', 0))
                weather_main = data['weather'][0].get('main', 'Unknown')
                timestamp = data.get('dt', 0)
                
                weather_data.append({
                    "city_id": city_id,
                    "temp": temp,
                    "feels_like": feels_like,
                    "main": weather_main,
                    "timestamp": timestamp
                })
            else:
                print(f"Warning: Data format unexpected for city_id {city_id}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for city_id {city_id}: {e}")
    return weather_data

def calculate_daily_summary(weather_data):
    if not weather_data:
        print("No data available for daily summary calculation.")
        return
    
    temps = [entry['temp'] for entry in weather_data]
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    weather_counts = {}
    for entry in weather_data:
        condition = entry['main']
        weather_counts[condition] = weather_counts.get(condition, 0) + 1
    dominant_condition = max(weather_counts, key=weather_counts.get)

    summary = {
        "average_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_condition": dominant_condition
    }
    return summary

if __name__ == "__main__":
    print("Fetching weather data...")
    weather_data = get_weather_data()
    daily_summary = calculate_daily_summary(weather_data)
    
    if daily_summary:
        print("\nDaily Weather Summary:")
        print(json.dumps(daily_summary, indent=4))
    else:
        print("Failed to compute the daily summary.")
