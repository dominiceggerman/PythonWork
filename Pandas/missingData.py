# Handling missing data
import numpy as np
import pandas as pd

if __name__ == "__main__":

    # Create Dataframe
    print("-- Original Frame --")
    df = pd.DataFrame({"A":[1,2,np.nan], "B":[5,np.nan,np.nan], "C":[1,2,3]})
    print(df)

    # Drop missing values
    print("-- Drop rows with missing values --")
    print(df.dropna(axis=0))
    print("-- Drop columns with missing values --")
    print(df.dropna(axis=1))

    # Threshhold for dropping
    print("-- Set threshhold for drop --")
    print(df.dropna(axis=0, thresh=2))

    # Replacing missing values with mean
    print("-- Replace NaN with mean of column --")
    print(df[:].fillna(value=df[:].mean()))
    
    

    
