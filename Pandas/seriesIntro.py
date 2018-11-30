# Overview of Series
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    data = [1,2,3]
    labels = ["a", "b", "c"]
    zipdic = dict(zip(labels, data))

    print(pd.Series(data, labels))
    print(pd.Series(zipdic))