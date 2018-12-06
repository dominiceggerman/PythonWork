# Overview of setting axis scales
from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # Data
    x = np.arange(0,100)

    # Set Figure and subplots
    fig = plt.figure()
    ax1, ax2 = fig.subplots(1, 2)
    
    # Normal scale
    ax1.plot(x, x**2)
    ax1.set_title("Normal scale")
    # Display xticks every 10
    ax1.set_xticks(np.arange(0,101,10))
    # Use scientific notation for yticks
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1,1))
    ax1.yaxis.set_major_formatter(formatter)

    # Log scale
    ax2.plot(x, x**2)
    ax2.set_yscale("log")
    ax2.set_title("Logarithmic and Normal scale")
    ax2.set_ylabel("Log Axis")
    # Custom grid
    ax2.grid(color="g", alpha=0.5, linestyle="dashed", linewidth=0.5, which="both")
    # Add second y axis
    axdual = ax2.twinx()
    axdual.plot(x, x, color="red")
    axdual.set_ylabel("Normal Axis")

    # Show plot
    plt.tight_layout()
    plt.show()