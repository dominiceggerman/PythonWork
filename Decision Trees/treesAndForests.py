# Decision Trees and Random Forests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    # Read Data
    df = pd.read_csv("Decision Trees/kyphosis.csv")

    # See relations
    sns.pairplot(df, hue="Kyphosis")
    plt.show()

    # Train / test
    x = df.drop("Kyphosis", axis=1)
    y = df["Kyphosis"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # Classify in decision tree
    print("Decision Tree:")
    dtree = DecisionTreeClassifier()
    dtree.fit(x_train, y_train)
    dtree_pred = dtree.predict(x_test)
    print(confusion_matrix(y_test, dtree_pred))
    print()
    print(classification_report(y_test, dtree_pred))

    # Random forest
    print("Random Forest:")
    rfc = RandomForestClassifier(n_estimators=200)
    rfc.fit(x_train, y_train)
    rfc_pred = rfc.predict(x_test)
    print(confusion_matrix(y_test, rfc_pred))
    print()
    print(classification_report(y_test, rfc_pred))