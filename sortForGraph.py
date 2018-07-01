# Sort one array, ascending, and sort other based on first array (matching indicies)
import numpy as np
import matplotlib.pyplot as plt

# Using standard lists
def sortLists(x, y):

    # Store indicies order of x 
    x_indicies = []
    for i in range(max(x) + 1):
        if i in x:
            x_indicies.append(x.index(i))

    # Sort the arrays using x_indicies
    x_sorted = [x[i] for i in x_indicies]
    y_sorted = [y[i] for i in x_indicies]

    # Graph
    plt.plot(x_sorted, y_sorted)
    plt.show()

# Using numpy
def sortNumpyArrays(x, y):

    # Store indicies order of x 
    x_indicies = np.array([], dtype="int32")
    for i in range(x.max() + 1):
        if True in (i == x):
            x_indicies = np.append(x_indicies, np.where(x==i)[0][0])

    # Sort the arrays using x_indicies
    x_sorted = x[x_indicies]
    y_sorted = y[x_indicies]

    # Graph
    plt.plot(x_sorted, y_sorted)
    plt.show()

# Execute
if __name__ == "__main__":

    # Unsorted arrays - x sorted asc
    x = [34, 108, 64, 88, 99, 51]
    y = [5, 17, 11, 8, 14, 5]
    # Unsorted arrays - numpy
    npx = np.array([34, 108, 64, 88, 99, 51])
    npy = np.array([5, 17, 11, 8, 14, 5])

    sortLists(x, y)
    sortNumpyArrays(npx, npy)
