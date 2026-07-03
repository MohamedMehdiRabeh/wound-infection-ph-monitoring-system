import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../data/pH.csv")
print(df.info())
plt.plot(df["Time"],df["pH"])
plt.axhspan(6, 6.5, color='#30D158', alpha=0.2, label="Healthy surgical site")
plt.axhspan(6.5, 7.2, color='#FFA94D', alpha=0.2, label="Infection risk")
plt.axhspan(7.2, 8, color='#FF6B6B', alpha=0.2, label="Infected Surgical Site")
plt.ylabel("pH of the surgical site")
plt.xlabel("Time (hours)")
plt.title("Simulated Wound pH Dynamics for Infection Progression Analysis")
plt.xticks(np.arange(0, 48, 12))
plt.legend()
plt.savefig("../outputs/wound_ph_plot.png")
plt.show()