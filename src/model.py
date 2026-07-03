import os
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(base_dir, "data", "pH.csv")
output_path = os.path.join(base_dir, "outputs", "labeled_ph_data.csv")

df = pd.read_csv(data_path)

def classify_ph(ph):
    if ph <= 6.5:
        return "Healthy"
    elif ph <= 7.2:
        return "Risk"
    else:
        return "Infected"

df["Status"] = df["pH"].apply(classify_ph)

df.to_csv(output_path, index=False)

print("Model completed.")