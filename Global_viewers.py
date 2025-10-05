import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("anime_watchers_dataset_10000.csv")

df = df.drop(columns=["Name","Favorite_Character","Device_Used_for_Watching","Year_of_Birth"])

group = df.groupby("Start_Year_Watching")
yearly_viewers = group["Watcher_ID"].count()
print(yearly_viewers)

#THIS CODE DOES THE SAME THING AS THE CODE ABOVE
#yearly_viewers = df['Start_Year_Watching'].value_counts().sort_index()
#print(yearly_viewers)

#PLOTTING THE DATA:
plt.figure(figsize=(10,6))
plt.plot(yearly_viewers.index, yearly_viewers.values, marker='o', linestyle='-', color='b')

# Titles and labels
plt.title("Anime Viewership Growth Over the Years", fontsize=14)
plt.xlabel("Year Started Watching", fontsize=12)
plt.ylabel("Number of New Viewers", fontsize=12)

# Grid for readability
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()