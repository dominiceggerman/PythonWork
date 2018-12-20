# Logistic Regression with SKLearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def imputeAge(cols):
    age = cols[0]
    Pclass = cols[1]

    if pd.isnull(age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return age
            

if __name__ == "__main__":
    # Data
    train = pd.read_csv("Sklearn/titanic_train.csv")
    
    # How many survived? By gender? By class?
    fig, axes = plt.subplots(1, 2)
    sns.countplot(x="Survived", data=train, hue="Sex", ax=axes[0])
    sns.countplot(x="Survived", data=train, hue="Pclass", ax=axes[1])
    plt.show()

    # Fill missing age data rather than drop
    fig, ax = plt.subplots(3, 1)
    fig.set_figwidth(8)
    fig.set_figheight(14)
    sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis", ax=ax[0])
    ax[0].set_title("Heatmap showing null values")
    sns.boxplot(x="Pclass", y="Age", data=train, ax=ax[1])
    ax[1].set_title("Showing age statistics by class")
    # Apply imputeAge() to training data, filling in the mean age per class for null values
    train["Age"] = train[["Age", "Pclass"]].apply(imputeAge, axis=1)
    # Show that data is filled
    sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis", ax=ax[2])
    ax[2].set_title("Heatmap showing filled values")
    plt.tight_layout()
    plt.show()

    # Prepare frame for training
    # Convert categorical data to quantitative
    sex = pd.get_dummies(train["Sex"], drop_first=True)
    embark = pd.get_dummies(train["Embarked"], drop_first=True)
    train = pd.concat([train, sex, embark], axis=1)
    train.drop(["Sex", "Embarked", "Name", "Ticket"], axis=1, inplace=True)
    # Create model
    x = train.drop("Survived", axis=1)
    y = train["Survived"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)
    logmodel = LogisticRegression()
    logmodel.fit(x_train, y_train)
    predictions = logmodel.predict(x_test)
    print(classification_report(y_test, predictions))