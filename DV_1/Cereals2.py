import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("cereal.csv")
df = df.dropna()
num_cols = ['Calories', 'Protein', 'Fat', 'Sodium', 'Fiber', 'Carbo', 'Sugars', 'Potass','Vitamins']

plt.figure(figsize=(12,8))
sns.boxplot(data=df[num_cols])
plt.title("Nutritional Distribution")
plt.show()

df[num_cols].hist(figsize=(12,8))
plt.suptitle("Nutritional Distribution")
plt.show()

df_sorted = df.sort_values(by="Rating")
df_sorted = pd.concat([df_sorted[:10],df_sorted[-10:]])

sns.barplot(x=df_sorted["Name"],y=df_sorted["Rating"])
plt.xticks(rotation=45,ha='right')
plt.title("Top and Bottom 10 Cereal Rating")
plt.xlabel("Cereals")
plt.ylabel("Rating")
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x=df_sorted["Sugars"],y=df_sorted["Rating"],hue=df_sorted["Name"])
plt.xticks(rotation=45,ha='right')
plt.title("Cereal Rating")
plt.xlabel("Sugar")
plt.ylabel("Rating")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

plt.figure(figsize=(12,6))
sns.regplot(x=df_sorted["Sugars"],y=df_sorted["Rating"])
plt.xticks(rotation=45,ha='right')
plt.title("Cereal Rating")
plt.xlabel("Sugar")
plt.ylabel("Rating")
plt.show()

grouped = df.groupby("Manuf")["Rating"].mean().reset_index()
sns.barplot(x=grouped["Manuf"],y=grouped["Rating"])
plt.xticks(rotation=45,ha='right')
plt.title("Manufacturer vs Rating")
plt.xlabel("Manufacturer")
plt.ylabel("Rating")
plt.show()

