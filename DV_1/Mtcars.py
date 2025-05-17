'''
1. For the MTCARS dataset, answer the specified questions with summarization and effective visuals.
a) Create a histogram to visualize the distribution of Miles Per Gallon (mpg).
b) Generate a boxplot for horsepower (hp) to identify outliers.
c) Plot a scatter plot between horsepower (hp) and mpg. What trend do you observe?
d) Create a bar chart showing the average mpg for each cylinder category (4, 6, 8 cylinders).
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mtcars.csv")

plt.figure(figsize=(12,6))
sns.histplot(x=df["model"],y=df["mpg"])
plt.xticks(rotation=45,ha='right')
plt.title("MPG Comparision")
plt.xlabel("Cars")
plt.ylabel("MPG")
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(df["hp"])
plt.title("Horsepower Boxplot")
plt.xlabel("Horsepower")
plt.ylabel("Values")
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x=df["hp"],y=df["mpg"],hue=df["model"])
plt.title("Horsepower vs MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

grouped = df.groupby("cyl")["mpg"].mean().reset_index()
plt.figure(figsize=(12,6))
sns.barplot(x=grouped["cyl"],y=grouped["mpg"])
plt.title("Cylinders vs MPG")
plt.xlabel("Cylinders")
plt.ylabel("MPG")
plt.show()
