# Grouping Data
import numpy as np
import pandas as pd

if __name__ == "__main__":

    # Data
    print("-- Original dataframe --")
    df = pd.DataFrame({'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]})
    print(df)

    # Group by company
    print("-- Group by company to get mean / sum / etc of sales --")
    byComp = df.groupby("Company")
    print(byComp.mean())
    print(byComp.sum())

    # Digging deeper
    print("-- Which person made the highest sales for each company --")
    print(df.groupby("Company").max())

    # Get in depth stats for each company
    print("-- .describe() method --")
    print(df.groupby("Company").describe().transpose())