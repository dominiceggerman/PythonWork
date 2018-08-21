# By Dominic Eggerman
import pandas as pd
import numpy as np
from dateutil import parser as dprs
import matplotlib.pyplot as plt

# Acquire data
def acquire(path):

    df = pd.read_csv(path)
    return df

# Sort
def sortData(df):

    # Get data
    dates = df["Effective Date"].values
    scheduled = df["Scheduled (BZ)"].values
    opcap = df["Operational (BZ)"].values
    # Reverse if needed
    if dprs.parse(dates[0]) < dprs.parse(dates[len(dates)-1]):
        dates = dates[::-1]
        scheduled = scheduled[::-1]
        opcap = opcap[::-1]

    # Transform data
    scheduled = scheduled / 1030
    opcap = opcap / 1030

    # Push to dataframe
    new_df = pd.DataFrame({"Date":dates, "Scheduled":scheduled, "Operational":opcap})
    return new_df


# Run
if __name__ == "__main__":
    title = "Wagoner East"
    path = "C:/Users/domin/Downloads/Wagoner East (2).csv"
    data = acquire(path)
    df = sortData(data)

    # Sorted data
    dates = df["Date"].values

    # Set up labels
    plt.title(title, fontsize=20)
    plt.ylabel("MMcf/d")
    plt.xticks(rotation=90)

    # Plot
    ax = plt.axes()
    ax.plot(dates, df.iloc[:,1:])  # plot all data vs dates
    
    ax.yaxis.grid(linestyle=":")
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)

    # Show
    plt.show()
