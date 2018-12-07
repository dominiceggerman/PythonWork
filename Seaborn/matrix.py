# Matrix plots with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Data
    tips = sns.load_dataset("tips")
    flights = sns.load_dataset("flights")

    # Correlation data
    tc = tips.corr()
    # Heat map with tips
    sns.heatmap(tc, annot=True, cmap="coolwarm")
    plt.title("Heat map of tips correlaton data")
    plt.tight_layout()
    plt.show()

    # Pivot flights and graph as heat map
    flights_piv = flights.pivot_table(index="month", columns="year", values="passengers")
    sns.heatmap(flights_piv, cmap="magma", linecolor="white", linewidth=1)
    plt.title("Heat map of flights pivot")
    plt.tight_layout()
    plt.show()

    # Cluster map
    sns.clustermap(flights_piv, standard_scale=1)
    plt.title("Cluster map of flights pivot (cluster based on similarity)")
    plt.tight_layout()
    plt.show()