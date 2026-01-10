import numpy as np
import pandas as pd 
path = r"local-repo\audi.csv"
df = pd.read_csv(path)
print(df.head())