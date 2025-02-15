"""
hi chat

the main issue is that not every patient listed in the patient survey (phenotypic labels) is in the main genetic data for some reason

this just finds the participants that are present in both data tables
"""

import pandas as pd

gd = pd.read_csv("genetic_data_unfiltered.csv")
ps = pd.read_csv("patient_survey_2015.csv")

gd_participants = [id for id in gd["Participant"]]

mutual_ids = []
for id in ps["Participant"]:
    if id in gd_participants:
        mutual_ids.append(id)

with open("mutual_ids.txt", 'a') as f:
    for id in mutual_ids:
        f.write(id + "\n")  

