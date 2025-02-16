import pandas as pd

pgp = pd.read_csv("Categorized_Disease_Data.csv")

print(len(pgp["Disease Category"].dropna().unique()))