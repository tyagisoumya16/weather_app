from flask import Flask, render_template, request
from api import get_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = None
    error = None

    if request.method == "POST":

        city = request.form["city"]

        data = get_weather(city)

        if data["cod"] != 200:
            error = "City not found!"

        else:
            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "condition": data["weather"][0]["description"],
                "wind": data["wind"]["speed"]
            }

    return render_template(
        "index.html",
        weather=weather_data,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)