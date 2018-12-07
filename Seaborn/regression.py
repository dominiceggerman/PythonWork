# Seaborn regression plots
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Data
    tips = sns.load_dataset("tips")

    # Linear regression
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", markers=["o", "v"])
    plt.title("Lmplot with hue=sex")
    plt.show()

    # Separate by columns
    sns.lmplot(x="total_bill", y="tip", data=tips, col="sex", markers=["o", "v"])
    plt.title("Lmplot with col=sex")
    plt.show()
