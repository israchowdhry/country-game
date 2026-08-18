# 🌍 Country Game

Country Game is an interactive Flask web application designed to help users learn and practice naming the **197 countries of the world**.

I originally started memorizing the countries of the world out of personal interest. While learning them, I decided to turn the process into a coding project that would help me practice geography while also developing my Python, data science, and web development skills.

## 🎮 How It Works

Users choose one of six continents:

- Africa
- Asia
- Europe
- North America
- South America
- Oceania

After selecting a continent, the user types country names into an input box.

The application checks each answer against a dataset containing 197 countries and their corresponding continents.

The application responds with:

- **Correct!** — the country belongs to the selected continent.
- **You already found this country!** — the country was previously entered.
- **Try again!** — the country is incorrect or belongs to another continent.

The application also tracks progress for each continent:

`Countries found: 5 / 12`

Correctly guessed countries are displayed on the page so users can keep track of the countries they have already identified.

## ✨ Features

- Dataset containing 197 countries
- Separate game for each continent
- Dynamic continent pages using Flask
- Case-insensitive country matching
- Handles accidental spaces in user input
- Prevents duplicate guesses
- Tracks progress separately for each continent
- Individual user progress using Flask sessions
- Displays correctly guessed countries
- Automatically calculates the number of countries in each continent
- Autofocus for quick keyboard-based guessing
- Ability to reset progress and start again
- Custom HTML and CSS interface
- Public deployment using Render

## 📊 Data Processing

The original country dataset is stored in CSV format with the following structure:

```text
Continent,Country
Africa,Algeria
Africa,Angola
Africa,Benin
...
```

I use **Pandas** to load, inspect, validate, and prepare the dataset before it is used by the Flask application.

The data preparation process includes:

- Loading CSV data with `pandas.read_csv()`
- Inspecting the dataset's rows and columns
- Checking for missing values
- Checking for duplicate rows
- Checking for duplicate country names
- Counting countries by continent
- Renaming columns to match the application's data structure
- Converting the cleaned CSV dataset into JSON

For example, the original columns:

```text
Continent
Country
```

are renamed to:

```text
continent
name
```

The cleaned data is then exported to `countries.json`, which is used by the Flask application.

### Data Pipeline

```text
Kaggle CSV Dataset
        ↓
    Pandas
        ↓
Data Inspection & Cleaning
        ↓
Column Transformation
        ↓
 JSON Conversion
        ↓
countries.json
        ↓
 Flask Application
        ↓
  Country Game
```

This allows the data preparation process to remain separate from the web application's main logic.

## 🛠️ Technologies Used

- **Python** — application logic and data processing
- **Pandas** — CSV loading, validation, cleaning, and transformation
- **Flask** — backend web framework
- **JSON** — processed country data used by the application
- **HTML** — webpage structure
- **CSS** — website styling
- **Jinja** — dynamic HTML templates
- **Git** — version control
- **GitHub** — source code hosting
- **Gunicorn** — production web server
- **Render** — application deployment

## 📁 Project Structure

```text
country_game/
│
├── app.py
├── convert_data.py
├── countries.csv
├── countries.json
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── continent.html
│
└── static/
    ├── style.css
    └── images/
```

### `app.py`

Contains the Flask application and game logic, including:

- Routes
- Country checking
- Continent filtering
- User sessions
- Score tracking
- Template rendering

### `convert_data.py`

Handles the data preparation process, including:

- Reading the CSV dataset
- Renaming columns
- Inspecting the data
- Checking missing values
- Checking duplicates
- Converting the cleaned data to JSON

### `countries.csv`

Contains the original country and continent dataset.

### `countries.json`

Contains the processed country data used by the Flask application.

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

### 4. Set the Flask secret key

The application uses a Flask session to keep each user's guesses separate.

Set a `SECRET_KEY` environment variable before running the application.

### 5. Run the data conversion script

If you want to regenerate `countries.json` from the CSV dataset:

```bash
python convert_data.py
```

### 6. Run the Flask application

```bash
python app.py
```

Then open the local address displayed in the terminal.

## 🧠 What I Learned

This project gave me hands-on practice with both data processing and web development.

### Python and Data

- Reading CSV files with Pandas
- Exploring DataFrames
- Working with lists and dictionaries
- Checking for missing values
- Detecting duplicate data
- Filtering datasets
- Renaming DataFrame columns
- Converting CSV data to JSON
- Working with structured JSON data
- Loops and conditional statements

### Flask and Web Development

- Creating Flask applications
- Creating dynamic routes
- Understanding GET and POST requests
- Processing HTML form input
- Passing Python variables to HTML
- Using Jinja templates
- Tracking user progress with Flask sessions
- Using environment variables for sensitive configuration
- Connecting backend logic with a frontend interface
- Styling webpages with CSS

### Development and Deployment

- Git version control
- GitHub repositories
- Managing Python dependencies
- Environment variables
- Deploying a Flask application with Render and Gunicorn

## 🔮 Future Improvements

Possible future additions include:

- Interactive maps for each continent
- Highlighting countries on the map as they are correctly guessed
- Timed challenges
- Personal best scores
- User statistics
- Data visualizations showing quiz performance
- Database storage for persistent user progress

## 🎯 Purpose

I originally started memorizing the 197 countries of the world out of personal interest. As I was learning them, I decided to create a website that could help me practice, keep track of the countries I had already learned, and make the memorization process more interactive.

I also wanted to use the project as an opportunity to strengthen my programming and data science skills. Instead of practicing concepts only through isolated exercises, this project allows me to work with a real dataset and apply Python, Pandas, Flask, JSON, HTML, and CSS to build something that I personally wanted to use.