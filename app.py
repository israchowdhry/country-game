from flask import Flask, render_template, request, session
import json
import os


# Create the Flask application
app = Flask(__name__)


# Get the secret key from an environment variable
# Flask uses this key to securely sign session cookies
app.secret_key = os.environ.get("SECRET_KEY")


# Open the JSON file and load the country data into Python
with open("countries.json", "r") as file:
    countries = json.load(file)


# Home page route
# When someone visits "/", display index.html
@app.route("/")
def home():
    return render_template("index.html")


# Dynamic route for each continent
# <continent_name> takes the continent name from the URL
# GET displays the page and POST processes a submitted country
@app.route("/continent/<continent_name>", methods=["GET", "POST"])
def continent(continent_name):

    # Start with an empty message when the page first loads
    message = ""


    # If this user does not have any guesses stored yet,
    # create an empty list for each continent in their session
    if "guessed_countries" not in session:
        session["guessed_countries"] = {
            "Africa": [],
            "Asia": [],
            "Europe": [],
            "North America": [],
            "South America": [],
            "Oceania": []
        }


    # Create a list that will contain only the countries
    # belonging to the continent the user selected
    continent_countries = []

    # Loop through all countries in the JSON dataset
    for country in countries:

        # Check whether the country belongs to the selected continent
        if country["continent"] == continent_name:
            continent_countries.append(country)


    # Get this user's previous correct guesses for the selected continent
    current_guesses = session["guessed_countries"][continent_name]


    # Only check for an answer when the user submits the form
    if request.method == "POST":

        # Get the country entered in the HTML form
        # strip() removes extra spaces from the beginning and end
        country = request.form["country"].strip()


        # Search through the countries belonging to this continent
        for item in continent_countries:

            # Convert both names to lowercase so capitalization does not matter
            if country.lower() == item["name"].lower():

                # Check whether the user already guessed this country
                if item["name"] in current_guesses:
                    message = "You already found this country!"

                else:
                    # Add the correct country to the user's guesses
                    current_guesses.append(item["name"])

                    # Tell Flask that the session data was changed
                    session.modified = True

                    message = "Correct!"

                # Stop searching because the country was found
                break

        # This else belongs to the for loop.
        # It runs if the loop finishes without finding a matching country.
        else:
            message = "Try again!"


    # Count the total number of countries in the selected continent
    total_countries = len(continent_countries)


    # Send the data to continent.html so it can be displayed
    return render_template(
        "continent.html",
        message=message,
        guessed_countries=current_guesses,
        total_countries=total_countries,
        continent_name=continent_name
    )


# Reset route
# Removes the user's saved guesses from their session
@app.route("/reset")
def reset():

    # Remove guessed_countries if it exists
    # None prevents an error if it does not exist
    session.pop("guessed_countries", None)

    # Return the user to the home page
    return render_template("index.html")


# Run the Flask development server when app.py is run directly
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True,
        use_reloader=False
    )
