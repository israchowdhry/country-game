import pandas as pd


# Read the CSV file and store the data in a Pandas DataFrame
df = pd.read_csv("countries.csv")


# Rename the columns to match the names used in the Flask application
df = df.rename(columns={
    "Continent": "continent",
    "Country": "name"
})


# Display the first 5 rows of the dataset
print(df.head())

# Display the number of rows and columns
print(df.shape)

# Check for missing values in each column
print(df.isnull().sum())

# Count how many countries belong to each continent
print(df["continent"].value_counts())


# Check for duplicate rows in the dataset
print("Duplicate rows:", df.duplicated().sum())

# Check for duplicate country names
print("Duplicate countries:", df["name"].duplicated().sum())


# Get each unique continent and loop through them
for continent in df["continent"].unique():
    print(f"\n{continent}")

    # Filter the DataFrame to include only countries
    # that belong to the current continent
    continent_data = df[df["continent"] == continent]

    # Print the name of each country in the current continent
    for country in continent_data["name"]:
        print(country)


# Convert the cleaned DataFrame into a JSON file
# orient="records" creates a list of dictionaries
# indent=4 makes the JSON file easier to read
df.to_json(
    "countries.json",
    orient="records",
    indent=4
)