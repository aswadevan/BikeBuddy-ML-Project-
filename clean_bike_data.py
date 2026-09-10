mport pandas as pd

df = pd.read_excel("ml project.xlsx", header=None)

df.columns = ["brand", "model", "kilometers", "year", "price", "owner"]

print("Unique brands:")
print(df["brand"].unique())

print("\nUnique owners:")
print(df["owner"].unique())

print("\nKilometers:")
print(df["kilometers"].describe())

print("\nYears:")
print(df["year"].describe())

print("\nPrices:")
print(df["price"].describe())
