# Incomplete overview of Numpy basics
import numpy as np

if __name__ == "__main__":
    
    # Linspace generates an array (len = arg #3) of evenly spaced points between arg #1 and #2
    print("Linspace array: ", np.linspace(0, 100, 25))

    # Generate an array and reshape as a matrix
    ranarr = np.random.randint(0, 100, 25)
    print("Random integer array: ", ranarr)
    print("Reshaped array: ", ranarr.reshape(5, 5))

    print("Max: {0} Indmax: {1} Min: {2} Indmin: {3}". format(np.max(ranarr), np.argmax(ranarr), np.min(ranarr), np.argmin(ranarr)))