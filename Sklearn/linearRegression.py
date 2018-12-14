# Linear Regression with SKLearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

if __name__ == "__main__":
    # Data
    df = pd.read_csv("Sklearn/USA_Housing.csv")
    
    # Split into training (for the model) and testing (once model is trained) datasets
    x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
    y = df["Price"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

    # Create and train model
    lm = LinearRegression()
    lm.fit(x_train, y_train)
    print("Intercept:", lm.intercept_)

    # Get coeffs of columns
    cdf = pd.DataFrame(lm.coef_, x.columns, columns=["Coeff"])
    print(cdf)
    print("With all other variables fixed, a unit increase of an item in the index is associated with an X unit (coeff) increase/decrease in the y variable (Price in $)")

    # Get predictions and display graphically
    pred = lm.predict(x_test)
    plt.scatter(y_test, pred)
    plt.title("Y-Test vs. Model Predictions")
    plt.show()

    # Metrics
    print("\nMetrics:")
    print("Mean abs error:", metrics.mean_absolute_error(y_test, pred))
    print("Mean squared error", metrics.mean_squared_error(y_test, pred))
    print("RMS error", np.sqrt(metrics.mean_squared_error(y_test, pred)))
    print("R squared:", metrics.explained_variance_score(y_test, pred))