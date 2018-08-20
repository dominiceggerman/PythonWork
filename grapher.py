# By Dominic Eggerman
import pandas as pd
import matplotlib.pyplot as plt

# Acquire data
def acquire(path):

    df = pd.read_csv(path)
    return df
    
def graphLastMonth(df):

    # Get data
    dates = df["Effective Date"].values
    scheduled = df["Scheduled (BZ)"].values
    opcap = df["Operational (BZ)"].values

    # Transform data
    scheduled = scheduled / 1030
    opcap = opcap / 1030

    # Plot
    plt.plot(dates, scheduled)
    plt.ylabel("MMcf/d")
    # plt.xticks()
    plt.show()


# Run
if __name__ == "__main__":
    path = "C:/Users/deggerman/Downloads/Wagoner East (2).csv"
    data = acquire(path)
    graphLastMonth(data)