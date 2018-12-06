# Distribution plots with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load in Seaborn dataset
    tips = sns.load_dataset("tips")

    # Univariate plot (kernal density estimate = kde)
    sns.distplot(tips["total_bill"], kde=False, bins=30).set_title("Univariate Plot")
    plt.tight_layout()
    plt.show()

    # Bivariate plots (jointplot)

    sns.jointplot(x="total_bill", y="tip", data=tips)
    plt.title("Bivariate plot with default scatter")
    plt.tight_layout()
    plt.show()

    sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    plt.title("Bivariate plot with Regression")
    plt.tight_layout()
    plt.show()

    sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
    plt.title("Bivariate plot with Hex density")
    plt.tight_layout()
    plt.show()

    sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
    plt.title("Bivariate plot with Kernel density")
    plt.tight_layout()
    plt.show()
    
    # Pairwise relationship plot across entire dataframe (quickly visualize data)
    # Does a jointplot of all combination of columns in a dataframe
    sns.pairplot(tips, hue="sex")
    plt.title("Pairwise plot")
    plt.tight_layout()
    plt.show()

    # Basic Rugplot - univariate - relates to distplot
    sns.rugplot(tips["total_bill"])
    plt.title("Basic Rugplot - Used to construct a Kernel Density Estimation plot")
    # Construct a KDE by mapping a normal distribution over each rug mark and summing the normal values
    plt.tight_layout()
    plt.show()