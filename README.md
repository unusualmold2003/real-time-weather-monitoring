# Real-Time Weather Monitoring System

## Overview

This application monitors real-time weather data for major metro cities in India and provides summarized weather insights using rollups and aggregates. The system retrieves data from the OpenWeatherMap API, aggregates it to generate daily summaries, and triggers alerts based on user-defined thresholds.

## Objectives

- Periodically fetch real-time weather data from OpenWeatherMap.
- Generate daily weather summaries, including average temperature, maximum, minimum, and dominant weather conditions.
- Allow configurable alert thresholds for temperature and weather conditions.

## Features

- **Weather Data Retrieval**: Retrieves weather data for specific Indian metros at a configurable interval.
- **Data Aggregation**: Processes the data to generate daily summaries and calculate aggregates.
- **Alert System**: Triggers alerts based on temperature thresholds.
- **Visual Display**: Displays daily summaries and triggered alerts on the console.

## Installation

1. Clone the repository and navigate to the App2 directory:
    ```bash
    git clone https://github.com/unusualmold2003/real-time-weather-monitoring.git
    cd App2
    ```

2. Install dependencies using:
    ```bash
    pip install requests
    ```

## Configuration

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/).
2. Update `API_KEY` in `main.py` with your key:
    ```python
    API_KEY = 'YOUR_API_KEY'
    ```

## Usage

1. Run the script to start fetching data and generating summaries:
    ```bash
    python main.py
    ```

## Code Structure

- **`kelvin_to_celsius(kelvin_temp)`**: Converts temperatures from Kelvin to Celsius.
- **`get_weather_data()`**: Fetches and parses weather data for specified cities.
- **`calculate_daily_summary(weather_data)`**: Aggregates weather data to produce a daily summary.

## Example Output

- **Daily Weather Summary**:
    ```json
    {
        "average_temp": 29.5,
        "max_temp": 32,
        "min_temp": 27,
        "dominant_condition": "Clear"
    }
    ```

- **Alerts**:
    - Triggered when a threshold (e.g., temperature > 35°C) is breached for two consecutive updates.

## Testing

1. Define configurable alert thresholds.
2. Simulate API responses for different scenarios to validate temperature conversions, daily summaries, and alert triggers.
