# 🌍 Country Game

Country Game is an interactive Flask web application designed to help users learn and practice naming the **197 countries of the world**.

I built this project to combine learning geography with practicing beginner Python, web development, and data-handling skills.

## 🎮 How It Works

Users choose a continent and try to name all of the countries that belong to it.

The available continents are:

- Africa
- Asia
- Europe
- North America
- South America
- Oceania

After choosing a continent, the user enters country names into the input box.

The application checks each answer against a JSON dataset containing the countries and their corresponding continents.

The application responds with:

- **Correct!** — the country is correct.
- **You already found this country!** — the country was previously entered.
- **Try again!** — the country is incorrect or belongs to another continent.

The user's progress is also displayed:

`Countries found: 5 / 12`

Correctly guessed countries appear on the page so users can keep track of what they have already found.

## ✨ Features

- Dataset containing 197 countries
- Separate game for each continent
- Dynamic continent pages using Flask
- Case-insensitive country matching
- Handles accidental spaces in user input
- Prevents duplicate guesses
- Tracks progress for each continent
- Displays correctly guessed countries
- Automatically calculates the number of countries in each continent
- Autofocus allows users to quickly type and submit answers
- Individual user progress with Flask sessions
- Option to reset progress and start again
- Custom HTML and CSS interface
- Deployed as a public web application

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **JSON**
- **HTML**
- **CSS**
- **Jinja**
- **Git**
- **GitHub**
- **Gunicorn**
- **Render**



## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd country-game
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python -m flask --app app run --debug
```

### 5. Open the application

Open the local address shown in the terminal, typically:

```text
http://127.0.0.1:5000
```

## 🧠 What I Learned

This project gave me hands-on practice with:

* Reading JSON files with Python
* Lists and dictionaries
* Loops and conditional statements
* Filtering datasets
* Dynamic Flask routes
* GET and POST requests
* Processing HTML form input
* Connecting Python backend logic with HTML
* Jinja templates
* Flask sessions
* HTML and CSS
* Git and GitHub version control
* Deploying a Flask application

For example, the application loads all 197 countries from a JSON dataset and filters them according to the continent selected by the user.

This allowed me to practice working with structured data while building an application with a practical purpose.

## 🔮 Future Improvements

I plan to continue developing the project with features such as:

* Interactive maps for each continent
* Highlighting countries on the map when they are correctly guessed
* Timed challenges
* Personal best scores
* User statistics
* Data visualizations showing quiz performance
* Database storage for persistent progress

## 🎯 Purpose

I originally started memorizing the 197 countries of the world out of personal interest. As I was learning them, I decided to turn the process into a coding project and build a website that could help me practice and track my progress.

This project gave me a way to combine a personal goal with hands-on programming experience. By building Country Game, I am able to practice geography while applying Python, Flask, JSON, HTML, CSS, and data-handling concepts to something I genuinely wanted to use.
