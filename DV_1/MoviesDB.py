import pandas as pd
data = {
    "Movie Name": [
        "Inception", "Interstellar", "The Dark Knight", "Titanic", "Avatar",
        "3 Idiots", "Dangal", "Zindagi Na Milegi Dobara", "Gully Boy", "Sholay"
    ],
    "Language": [
        "English", "English", "English", "English", "English",
        "Hindi", "Hindi", "Hindi", "Hindi", "Hindi"
    ],
    "Genre": [
        "Sci-Fi", "Sci-Fi", "Action", "Romance", "Sci-Fi",
        "Comedy", "Drama", "Adventure", "Musical", "Action"
    ],
    "Rating": [
        8.8, 8.6, 9.0, 7.9, 7.8,
        8.4, 8.3, 8.2, 8.1, 8.2
    ],
    "Review": [
        "Mind-bending thriller", "Epic space odyssey", "Best Batman movie", "Emotional and timeless", "Visually stunning",
        "Entertaining and insightful", "Inspiring biopic", "Feel-good travel movie", "Street rap masterpiece", "Classic action-drama"
    ]
}
data = pd.DataFrame(data)
data.to_csv("Movies.csv")
df = pd.read_csv("Movies.csv")
print(df)

max_rating = df.loc[df["Rating"].idxmax(),["Movie Name","Rating"]]
print(f"The movie with the highest rating is :\n{max_rating}")

hindi_df = df.loc[df["Language"]=="Hindi"]
hindi_df.to_csv("Hindi_Movies.csv")

