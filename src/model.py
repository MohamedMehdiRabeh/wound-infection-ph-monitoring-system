import pandas as pd
df = pd.read_csv("../data/pH.csv")
def classify_ph(ph):
    if ph <= 6.5 :
        return "Healthy"
    if ph <= 7.2 :
        return "Risk"
    else :
        return "Infected"
df["Status"] = df["pH"].apply(classify_ph)
df.to_csv("../outputs/labeled_ph_data.csv", index=False)
