# Using recommender systems to recommend films
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Data
    df = pd.read_csv("Recommender Systems/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])
    titles = pd.read_csv("Recommender Systems/Movie_id_Titles")
    df = pd.merge(df, titles, on="item_id")
    print(df.head())

    print()

    # Group on ratings
    ratings = pd.DataFrame(df.groupby("title")["rating"].mean())
    ratings["num of ratings"] = pd.DataFrame(df.groupby("title")["rating"].count())
    print(ratings.head())

    print()

    # Get into matrix
    movmat = df.pivot_table(index="user_id", columns="title", values="rating")
    # Get Contact user ratings
    contact_ratings = movmat["Contact (1997)"]
    # Correlate with other movies
    corr_contact = pd.DataFrame(movmat.corrwith(contact_ratings), columns=["Correlation"])
    corr_contact.dropna(inplace=True)
    # Filter out movies that do not have at least 30 ratings
    corr_contact = corr_contact.join(ratings["num of ratings"])
    corr_contact = corr_contact[corr_contact["num of ratings"] > 30].sort_values("Correlation", ascending=False)
    print(corr_contact.head())
