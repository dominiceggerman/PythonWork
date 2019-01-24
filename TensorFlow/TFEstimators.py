# Using TensorFlow Estimators
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf


if __name__ == "__main__":
    # Data
    df = pd.read_csv("TensorFlow/iris.csv")
    df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "target"]
    df["target"] = df["target"].apply(int)
    y = df["target"]
    x = df.drop("target", axis=1)

    # Train / test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Create feature columns
    feat_cols = [tf.feature_column.numeric_column(col) for col in x.columns]
    
    # Create estimator
    input_func = tf.estimator.inputs.pandas_input_fn(x=x_train, y=y_train, batch_size=10, num_epochs=5, shuffle=True)
    classifier = tf.estimator.DNNClassifier(hidden_units=[10,20,10], n_classes=3, feature_columns=feat_cols)
    classifier.train(input_fn=input_func, steps=50)
    pred_fn = tf.estimator.inputs.pandas_input_fn(x=x_test, batch_size=len(x_test), shuffle=False)
    predictions = list(classifier.predict(input_fn=pred_fn))
    final_preds = [pred["class_ids"][0] for pred in predictions]
    print(confusion_matrix(y_test, final_preds))
    print(classification_report(y_test, final_preds))