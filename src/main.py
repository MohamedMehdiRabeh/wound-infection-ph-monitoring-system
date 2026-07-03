import os

print("Starting biomedical pipeline...\n")

os.system("python model.py")
os.system("python plot.py")
os.system("python summary.py")

print("\nPipeline completed. Outputs saved.")