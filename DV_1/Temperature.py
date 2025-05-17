import numpy as np 
import pandas as pd
Temp = pd.Series([32,27,40,34,23,34,37], index = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

print(Temp)
mean_temp = Temp.mean()
max_temp = Temp.max()
min_temp = Temp.min()
n = int(input("Enter specific value of Temperature : "))
above = Temp[Temp>n]
print(f"Average T : {mean_temp}\nMaximum T : {max_temp} on {Temp.idxmax()}\nMinimum T : {min_temp} on {Temp.idxmin()}\nT above input value :\n{above}")
faren = Temp*1.8 + 32
print(f"The T in Farenheit is :\n{faren}")
above_days = Temp[Temp>mean_temp].index
print("The T is above average on days : ")
print(above_days)