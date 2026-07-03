import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

base_dir = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(base_dir, "outputs", "labeled_ph_data.csv")
output_path = os.path.join(base_dir, "outputs", "wound_ph_plot.png")

df = pd.read_csv(data_path)

plt.figure(figsize=(10, 5))

plt.plot(df["Time"], df["pH"], color="black")

plt.axhspan(6, 6.5, color='#30D158', alpha=0.2)
plt.axhspan(6.5, 7.2, color='#FFA94D', alpha=0.2)
plt.axhspan(7.2, 8, color='#FF6B6B', alpha=0.2)

plt.xlabel("Time (hours)")
plt.ylabel("pH")
plt.title("Simulated Wound pH Dynamics")

plt.xticks(np.arange(0, 49, 12))

plt.savefig(output_path)
plt.show()

print("Plot completed.")