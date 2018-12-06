# Overview of Subplots with Matplotlib
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # Data
    x = np.arange(0,100)
    y = x*2
    z = x**2

    # Create figure
    fig = plt.figure()
    # Create subplots and map to axes
    ax1, ax2 = fig.subplots(nrows=1, ncols=2)
    # Plot
    ax1.plot(x,y)
    ax2.plot(x,z)
    # Show
    plt.tight_layout()
    plt.show()