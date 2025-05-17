import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("ipl.csv")

plt.figure(figsize=(12,8)) 
sns.boxplot(x="over",y="total_runs",data = df)
plt.title("Overs vs Runs")
plt.show()

plt.figure(figsize=(12,8)) 
top_bat = df.groupby('batter')['batsman_runs'].sum().sort_values(ascending = False).head(10).reset_index()
plt.bar(top_bat['batter'],top_bat['batsman_runs'])
plt.title("Top 10 Batsmen")
plt.xlabel("Batsmen")
plt.ylabel("Total Runs") 
plt.xticks(rotation = 45) 
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x=df['extras_type'],data=df,order=df['extras_type'].value_counts().index)
plt.title("Extra Runs")
plt.xlabel("Extra Type")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,8)) 
dismissal = df['dismissal_kind'].value_counts() 
plt.pie(dismissal,labels=dismissal.index)
plt.title("Dismissal Ratio")
plt.show()

bowler_data = df.groupby('bowler').agg({'total_runs':'sum','over':'count'}).reset_index() 
bowler_data['economy'] = bowler_data['total_runs']/bowler_data['over']
sns.scatterplot(x=bowler_data['over'],y=bowler_data['economy'])
plt.title("Bowler Economy")
plt.xlabel("Over")
plt.ylabel("Economy")
plt.show()


