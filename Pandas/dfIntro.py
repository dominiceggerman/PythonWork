# Overview of Dataframes
import numpy as np
import pandas as pd

if __name__ == "__main__":

    # Create dataframe
    print("-- Raw Frame --")
    df = pd.DataFrame(np.random.randn(5,5), index=["a", "b", "c", "d", "e"], columns=["L", "M", "N", "O", "P"])
    print(df)

    print("-- Dropping --")

    # Selecting multiple columns
    df[["L", "M"]]

    # Drop using inplace (don't have to reassign)
    df.drop("e", inplace=True)
    print(df)

    print("-- Boolean array --")

    # Create boolean array based on query
    booldf = df > 0
    # Pass bool to df to get NaN for false values
    df[booldf]
    print(df[df > 0])
    # Use for conditional selection
    print(df[df["L"] > 0])

    print("-- Comparison --")

    # Boolean series comparison (&)
    print(df[(df["M"] > 0) & (df["N"] < 0)])
    print(df[(df["M"] > 0) | (df["N"] < 0)])
