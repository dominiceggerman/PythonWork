# Basic Pandas Operations
import numpy as np
import pandas as pd

def times2(x):
    return x*2

if __name__ == "__main__":

    # Create dataframes
    print("\n-- Dataframe 1 --\n")
    df = pd.DataFrame({'col1':[1,2,3,4],
                    'col2':[444,555,666,444],
                    'col3':['abc','def','ghi','xyz']})
    print(df)

    # Unique values
    print("-- Unique values and value count in col2 --")
    print("array:", df["col2"].unique(), "| length():", df["col2"].nunique())
    print(df["col2"].value_counts())

    # Apply custom function to df
    print("-- Applying custom function to dataframe --")
    print(df["col1"].apply(times2))
    # print(df["col1"].apply(lambda x: x*2))

    # Get column names
    print("-- Get dataframe information --")
    print("Columns: ", df.columns)
    print("Index: ", df.index)

    # Sorting
    print("-- Sorting --")
    print(df.sort_values("col2"))


    print("\n-- Dataframe 2 --\n")
    df2 = pd.DataFrame({'A':['foo','foo','foo','bar','bar','bar'],
                    'B':['one','one','two','two','one','one'],
                    'C':['x','y','x','y','x','y'],
                    'D':[1,3,2,5,4,1]})
    print(df2)

    # Create multi-index
    print("-- Multi-index (pivot table) --")
    print(df2.pivot_table(values="D", index=["A", "B"], columns=["C"]))
    