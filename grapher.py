# By Dominic Eggerman
import pandas as pd
import numpy as np
from dateutil import parser as dprs
import matplotlib.pyplot as plt

# Acquire data
def acquire(path):

    df = pd.read_csv(path)
    return df
    
def graphLastMonth(df):

    # Sort
    # df.sort_values(by="Effective Date")

    # Get data
    dates = df["Effective Date"].values
    scheduled = df["Scheduled (BZ)"].values
    opcap = df["Operational (BZ)"].values
    if dprs.parse(dates[0]) < dprs.parse(dates[len(dates)-1]):
        dates = dates[::-1]
        scheduled = scheduled[::-1]
        opcap = opcap[::-1]

    # Transform data
    scheduled = scheduled / 1030
    opcap = opcap / 1030

    # Set up labels
    plt.ylabel("MMcf/d")
    plt.xticks(rotation=60)

    # Plot
    ax1 = plt.axes()
    # ax2 = plt.axes()
    ax1.plot(dates, scheduled)
    # ax2.plot(opcap)
    for label in ax1.xaxis.get_ticklabels()[::1]:
        label.set_visible(False)

    # Show
    plt.show()


# Run
if __name__ == "__main__":
    path = "C:/Users/deggerman/Downloads/Wagoner East (2).csv"
    data = acquire(path)
    graphLastMonth(data)