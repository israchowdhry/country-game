from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("countries.json", "r") as file:
    countries = json.load(file)

guessed_countries = {
    "Africa": [],
    "Asia": [],
    "Europe": [],
    "North America": [],
    "South America": [],
    "Oceania": []
}

# when someone visits (/), run the function underneath
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/continent/<continent_name>", methods=["GET", "POST"])
def continent(continent_name):
    message = ""

    continent_countries = []

    for country in countries:
        if country["continent"] == continent_name:
            continent_countries.append(country)

    current_guesses = guessed_countries[continent_name]

    if request.method == "POST":
        country = request.form["country"].strip()

        for item in continent_countries:
            if country.lower() == item["name"].lower():

                if item["name"] in current_guesses:
                    message = "You already found this country!"
                else:
                    current_guesses.append(item["name"])
                    message = "Correct!"

                break

        else:
            message = "Try again!"

    total_countries = len(continent_countries)

    return render_template(
        "continent.html",
        message=message,
        guessed_countries=current_guesses,
        total_countries=total_countries,
        continent_name=continent_name
    )

if __name__ == '__main__':
    app.run()