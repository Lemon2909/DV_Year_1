import pandas as pd
import numpy as np

df = pd.read_csv("cereal.csv")
df = df.drop(columns=["Cold","Nabisco","Quaker","Kelloggs","GeneralMills","Ralston","AHFP"])

five_num = df.describe().loc[['min', '25%', '50%', '75%', 'max']]
five_num.index = ['Minimum', 'First Quartile', 'Median', 'Second Quartile', 'Maximum']

df = df.fillna(-1)

df = df.replace(-1, df.median(numeric_only=True))

five_num_new = df.describe().loc[['min', '25%', '50%', '75%', 'max']]
five_num_new.index = ['Minimum', 'First Quartile', 'Median', 'Second Quartile', 'Maximum']

print(five_num_new)
