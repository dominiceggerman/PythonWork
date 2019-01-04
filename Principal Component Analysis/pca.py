# Principal component analysis with Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

if __name__ == "__main__":
    # Data
    cancer = load_breast_cancer()
    df = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
    print(df.head())

    # Preprocess data (scale)
    scaler = StandardScaler()
    scaler.fit(df)
    scaled_data = scaler.transform(df)

    # PCA
    pca = PCA(n_components=2)
    pca.fit(scaled_data)
    x_pca = pca.transform(scaled_data)
    print("Scaled data shape:", scaled_data.shape, "Principle component shape:", x_pca.shape)

    # Plot
    plt.scatter(x_pca[:, 0], x_pca[:, 1], c=cancer["target"], cmap="plasma")
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.tight_layout()
    plt.show()

    # Relation of principle components
    df_comp = pd.DataFrame(pca.components_, columns=cancer["feature_names"])
    sns.heatmap(df_comp, cmap="plasma")
    plt.tight_layout()
    plt.show()