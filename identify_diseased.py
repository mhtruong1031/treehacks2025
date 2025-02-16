import pandas as pd
import matplotlib.pyplot as plt


pgp = pd.read_csv("Categorized_Disease_Data.csv")

is_diseased = []
for row, data in pgp.iterrows():
    is_diseased.append(type(data.iloc[6]) != float and 'no' not in data.iloc[6].lower())

pgp["Is Diseased"] = is_diseased

pgp.to_csv("Diseased_Data_w_Bool.csv")

