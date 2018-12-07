# Categorical plots with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Data
    tips = sns.load_dataset("tips")

    # Basic bar plot
    sns.barplot(x="sex" , y="total_bill", data=tips, estimator=np.std)
    plt.title("Basic Bar plot")
    plt.tight_layout()
    plt.show()

    # Count plot
    sns.countplot(x="sex", data=tips)
    plt.title("Count plot")
    plt.tight_layout()
    plt.show()

    # Box plot
    sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
    plt.title("Box plot")
    plt.tight_layout()
    plt.show()

    # Violin plot
    sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
    plt.title("Violin plot")
    plt.tight_layout()
    plt.show()

    # Strip plot
    sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, split=True)
    plt.title("Strip plot")
    plt.tight_layout()
    plt.show()

    # Swarm plot
    sns.swarmplot(x="day", y="total_bill", data=tips)
    plt.title("Swarm plot (Similar to violin)")
    plt.tight_layout()
    plt.show()

    # Factor plot
    sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", kind="bar")
    plt.title("Factor plot (kind=bar)")
    plt.tight_layout()
    plt.show()