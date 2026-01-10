
import numpy as np
import pandas as pd 
path = r"C:\Users\ADMIN\OneDrive\Desktop\git-demo\local-repo\audi.csv"
df = pd.read_csv(path)
#print(df.head())
#print(df.info())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
print(df.describe())