# Fill between graph
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # Data
    x = np.arange(0,11)

    # Figure
    fig = plt.figure()
    ax1 = fig.subplots(1,1)

    # Fill between graph
    ax1.fill_between(x, x**2, x**3, color="red", alpha=0.5)

    # Show
    plt.tight_layout()
    plt.show()