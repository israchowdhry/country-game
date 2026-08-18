from flask import Flask, render_template, request, session
import json
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

with open("countries.json", "r") as file:
    countries = json.load(file)

# when someone visits (/), run the function underneath
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/continent/<continent_name>", methods=["GET", "POST"])
def continent(continent_name):
    message = ""

    if "guessed_countries" not in session:
        session["guessed_countries"] = {
            "Africa": [],
            "Asia": [],
            "Europe": [],
            "North America": [],
            "South America": [],
            "Oceania": []
        }

    continent_countries = []

    for country in countries:
        if country["continent"] == continent_name:
            continent_countries.append(country)

    current_guesses = session["guessed_countries"][continent_name]

    if request.method == "POST":
        country = request.form["country"].strip()

        for item in continent_countries:
            if country.lower() == item["name"].lower():

                if item["name"] in current_guesses:
                    message = "You already found this country!"
                else:
                    current_guesses.append(item["name"])
                    session.modified = True
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

@app.route("/reset")
def reset():
    session.pop("guessed_countries", None)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()