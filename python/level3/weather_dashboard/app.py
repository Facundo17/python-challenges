"""
Today we will build the following weather dashboard web app:

references/dashboard.png

Users can search for a city in the text box and the current weather information for that city will be displayed below the button:

references/dashboard2.png

You can use the Open Weather API to get current weather data. 
You need to sign up for a free account and get an API key. 
Then, build a Flask web app that makes API requests to 
the http://api.openweathermap.org/data/2.5/weather endpoint and display the received JSON data to the webpage.

Required Libraries: requests, flask
pip install flask requests
"""

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your OpenWeather API key
API_KEY = "YOUR API KEY"

def get_weather(city):
    """Fetch weather data for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    if request.method == "POST":
        city = request.form["city"]

        response = get_weather(city)

        if response:
            data = response
            weather_info = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather_info = {"error": "Ciudad no encontrada. Intenta de nuevo."}

    return render_template("index.html", weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True, host=5002)