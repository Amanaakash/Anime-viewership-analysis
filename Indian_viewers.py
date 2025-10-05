import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("anime_watchers_dataset_10000.csv")
df = df.drop(columns=["Name","Favorite_Character","Device_Used_for_Watching","Year_of_Birth"])

countryWise = df.groupby(["Country", "Start_Year_Watching"]).size()
India_viewers = countryWise.xs("India")

#plotting
plt.figure(figsize=(10,6))
plt.plot(India_viewers.index, India_viewers.values, marker='o', linestyle='-', color='b')

#titles and labels
plt.title("Anime viewership growth over the years in INDIA", fontsize=14)
plt.xlabel("Year Started Watching", fontsize=12)
plt.ylabel("Number of New Viewers", fontsize=12)

#grid for readability
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()