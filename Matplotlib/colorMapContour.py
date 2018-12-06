# Colormap and contour graph
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


if __name__ == "__main__":
    # Data
    m = np.linspace(0, np.pi, 100)
    n = np.linspace(0, 2*np.pi, 100)
    x, y = np.meshgrid(m, n)
    z = x * y
    
    # Figure
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    
    # ColorMap
    p = ax[0].pcolor(x, y, z, cmap=cm.RdBu, vmin=abs(z).min(), vmax=abs(z).max())
    cb = fig.colorbar(p, ax=ax[0])

    # Contour
    cnt = ax[1].contour(z, cmap=cm.RdBu, vmin=abs(z).min(), vmax=abs(z).max(), extent=[0, 1, 0, 1])

    # Show
    plt.tight_layout()
    plt.show()