import os
print("Starting biomedical pipeline...")
os.system("python model.py")
os.system("python plot.py")
print("Pipeline completed: results saved in outputs/")