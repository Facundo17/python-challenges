"""
For this project, we will build a RESTful API using FastAPI that simulates a simple weather forecast service.
This API will allow users to request a weather forecast for a specified city over a 3-day period.
Additionally, users can retrieve the weather forecast for a specific day within this period.
The purpose of this project is to introduce you to API development using 'FastAPI', which is a modern, fast (high-performance) web framework for building APIs with Python 3.6 and above.

The user can query 3-day forecast data for different cities:

For example, visiting http://127.0.0.1:8000/forecast/Chicago will return 3-day forecasts.

The user can also query a certain day in the next 3 days. 
For example, querying day 2 by visiting http://127.0.0.1:8000/forecast/Chicago/2.

Required Libraries: fastapi, unicorn
pip install fastapi uvicorn

Running the API: To run the API, you need to execute:

uvicorn weather_api:app --reload

where 'weather_api' is the name of your Python script and app is the name of the variable associated to the 'FastAPI()' instance
"""

from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Sample weather conditions for simulation
weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Stormy",
    "Snowy",
    "Windy",
    "Foggy"
]

# Fake data for forecast simulation
fake_forecast_data = [
    {
    "city": "new york",
    "forecasts": [
        {"day": 1, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 2, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 3, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)}
    ]
    },
    {
    "city": "los angeles",
    "forecasts": [
        {"day": 1, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 2, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 3, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)}
    ],
    },
    {
    "city":"chicago",
    "forecasts": [
        {"day": 1, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 2, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)},
        {"day": 3, "condition": choice(weather_conditions), "temperature_c": randint(20, 30)}
    ]
    }
]

@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Weather API is running"}

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    """
    Get a 3-day weather forecast for a specific city.
    """
    
    forecasts = next((item for item in fake_forecast_data if item['city'] == city_name.lower()), None)
    
    return {"data": forecasts if forecasts else "No data available for this city."}

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    """
    Get the weather forecast for a specific day in a 3-day forecast.
    """
    
    if day < 1 or day > 3:
        return {"error": "Day must be between 1 and 3."}
    
    forecasts = next((item for item in fake_forecast_data if item['city'] == city_name.lower()), None)
    
    if forecasts:
        forecastDay = {
            "city": forecasts['city'],
            "forecast": forecasts['forecasts'][day - 1] if forecasts else None
        }
    else:
        forecastDay = None
    
    
    return {"data": forecastDay if forecastDay else "No data available for this city."}
    