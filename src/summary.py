import os
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(base_dir, "outputs", "labeled_ph_data.csv")
output_path = os.path.join(base_dir, "outputs", "summary.txt")

df = pd.read_csv(data_path)

summary = ""

infection_rows = df[df["Status"] == "Infected"]

if not infection_rows.empty:
    infection_time = infection_rows["Time"].iloc[0]
    summary += f"Infection detected at {infection_time} hours.\n"
else:
    summary += "No infection detected.\n"

threshold_rows = df[df["pH"] > 7.2]

if not threshold_rows.empty:
    threshold_time = threshold_rows["Time"].iloc[0]
    summary += f"pH crossed 7.2 threshold at {threshold_time} hours.\n"
else:
    summary += "pH never exceeded infection threshold.\n"

with open(output_path, "w") as f:
    f.write(summary)

print("Summary completed.")