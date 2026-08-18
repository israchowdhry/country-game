import pandas as pd

df = pd.read_csv("countries.csv")

df = df.rename(columns={
    "Continent": "continent",
    "Country": "name"
})

print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df["continent"].value_counts())

print("Duplicate rows:", df.duplicated().sum())
print("Duplicate countries:", df["name"].duplicated().sum())

for continent in df["continent"].unique():
    print(f"\n{continent}")

    continent_data = df[df["continent"] == continent]

    for country in continent_data["name"]:
        print(country)

df.to_json(
    "countries.json",
    orient="records",
    indent=4
)