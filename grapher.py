# By Dominic Eggerman
# Imports
import pandas as pd
import numpy as np
from dateutil import parser as dprs
import matplotlib.pyplot as plt
import getpass

# Acquire data
def acquire(path):
    # Read file into dataframe and return
    df = pd.read_csv(path)
    return df

# Sort and filter the data
def sortData(df, pointName):
    # Get dates
    dates = df["Effective Date"].values
    # Get scheduled and opcap - turn to absolute values
    scheduled = np.absolute(df["Scheduled (BZ)"].values)
    opcap = np.absolute(df["Operational (BZ)"].values)
    # Reverse the array if needed (oldest to newest)
    if dprs.parse(dates[0]) > dprs.parse(dates[len(dates)-1]):
        dates = dates[::-1]
        scheduled = scheduled[::-1]
        opcap = opcap[::-1]

    # Transform data to MMcf
    scheduled = scheduled / 1030
    opcap = opcap / 1030

    # Push to new dataframe and return (cutting out other columns)
    new_df = pd.DataFrame({"Date":dates, 
                            "{} Scheduled".format(pointName):scheduled, 
                            "{} Operational".format(pointName):opcap
                            })
    return new_df


# Run
if __name__ == "__main__":
    # Get username
    user = getpass.getuser()
    # Graph title, file paths, and point names
    title = "Wagoner East vs Ramapo AGT"
    files = ["C:/Users/{}/Downloads/Wagoner East (2).csv".format(user), 
            "C:/Users/{}/Downloads/RAMAPO AGT (1).csv".format(user)
            ]
    points = ["Wagoner", "Ramapo"]
    # df is a list of dataframes - each index in df is data from a file in files
    df = [acquire(file) for file in files]
    df = [sortData(d, point) for d, point in zip(df, points)]

    # Set graph labels
    plt.title(title, fontsize=20)
    plt.ylabel("MMcf/d")
    plt.xticks(fontsize=8, rotation=90)

    # Pull longest range of dates
    dates = df[0]["Date"].values

    # Loop through dataframes and plot
    ax = plt.axes()
    for (ind, datafile) in enumerate(df):
        lineLabel = datafile.columns.values
        ax.plot(dates, datafile.iloc[:,1:], label=lineLabel[1])  # plot data vs dates
        ax.legend()  # set legend
    
    # Style gridlnes and xticks
    ax.yaxis.grid(linestyle=":")
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)

    # Show plot
    plt.tight_layout()
    plt.show()
