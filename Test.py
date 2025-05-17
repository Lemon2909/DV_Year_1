import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = {
    'Match_ID': np.arange(1, 11),
    'Country1': ['India', 'England', 'Australia', 'India', 'England', 'Pakistan', 'Australia', 'Pakistan', 'England', 'India'],
    'Country2': ['Australia', 'Pakistan', 'England', 'Pakistan', 'India', 'Australia', 'India', 'England', 'Australia', 'Pakistan'],
    'Score.Country1': [185, 160, 200, 175, 170, 155, 190, 180, 200, 185],
    'Score.Country2': [175, 165, 190, 160, 180, 165, 195, 170, 210, 180],
    'Winner': ['India', 'Pakistan', 'Australia', 'India', 'India', 'Australia', 'India', 'Pakistan', 'Australia', 'India']
}
df = pd.DataFrame(df)

'''plt.figure(figsize=(12,8))
total_runs = pd.DataFrame({"Country" : ["Country1","Country2"], "Runs" : [df["Score.Country1"].sum(),df["Score.Country2"].sum()]})
sns.barplot(data=total_runs,x="Country",y="Runs") 
plt.xlabel("Country")
plt.ylabel("Runs")
plt.show()'''

'''win_count = df["Winner"].value_counts()
plt.pie(win_count,labels = win_count.index)
plt.title("Percentage of Wins")
plt.show()'''

'''plt.figure(figsize=(12,8))
sns.barplot(data=df,x="Country1",y="Score.Country1")
plt.xlabel = "Countries"
plt.ylabel = "Runs"
plt.show()'''

plt.figure(figsize=(12,8))
sns.scatterplot(x=df["Score.Country1"],y=df["Score.Country2"])
plt.title("Country1 vs Country2 Scores")
plt.xlabel("Country 1 Scores")
plt.ylabel("Country 2 Scores")
plt.show()



