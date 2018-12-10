# DataVis with Pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Pandas will now use seaborn style

if __name__ == "__main__":
    # Data
    df1 = pd.read_csv("Pandas/df1", index_col=0)
    df2 = pd.read_csv("Pandas/df2")
    df3 = pd.read_csv("Pandas/df3")

    # Plot off of the dataframe
    df1["A"].plot(kind="hist", bins=30)
    plt.show()

    # Area plot
    df2.plot.area(alpha=0.7)
    plt.show()
    # df.plot.kind()