# Seaborn grids and subplots
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Data
    iris = sns.load_dataset("iris")
    tips = sns.load_dataset("tips")

    # Basic pairplot the data (iris)
    sns.pairplot(iris)
    plt.title("Basic pairplot of data")
    plt.tight_layout()
    plt.show()

    # Pair grid with iris
    gr = sns.PairGrid(iris)
    # Map the grid
    gr.map_diag(sns.distplot)
    gr.map_upper(plt.scatter)
    gr.map_lower(sns.kdeplot)

    plt.title("Plots using pair grid")
    plt.tight_layout()
    plt.show()


    # Facet grid with tips
    g = sns.FacetGrid(data=tips, col="time", row="smoker")
    g.map(sns.distplot, "total_bill")
    plt.title("Plots using facet grid")
    plt.tight_layout()
    plt.show()