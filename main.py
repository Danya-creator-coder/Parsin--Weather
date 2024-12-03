from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "84e63e52c18b0c1d37059306f2f63135"

@app.route("/")
def home():
    city = "Kyiv"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "temp": data["main"].get("temp"),
            "description": data["weather"][0].get("description").lower(),
        }

        is_hot = weather_data["temp"] >= 25
        is_rainy_or_snowy = "rain" in weather_data["description"] or "snow" in weather_data["description"]
        is_cold = weather_data["temp"] < 0

        return render_template("index.html", is_hot=is_hot, is_rainy_or_snowy=is_rainy_or_snowy, is_cold=is_cold)


@app.route("/weather")
def weather():
    city = "Kyiv"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "city": data.get("name"),
            "country": data["sys"].get("country"),
            "temperature": data["main"].get("temp"),
            "feels_like": data["main"].get("feels_like"),
            "description": data["weather"][0].get("description").capitalize(),
            "humidity": data["main"].get("humidity"),
            "pressure": data["main"].get("pressure"),
            "wind_speed": data["wind"].get("speed"),
            "icon": data["weather"][0].get("icon"),
        }

        return render_template("weather.html", weather=weather_data)



if __name__ == "__main__":
    app.run(port=20000, debug=True)