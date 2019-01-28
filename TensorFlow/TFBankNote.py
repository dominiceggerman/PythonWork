# Bank note authenticator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf


if __name__ == "__main__":
    # Data
    df = pd.read_csv("TensorFlow/bank_note_data.csv")

    # Visualize
    sns.pairplot(df, hue="Class")
    plt.show()

    # Standard Scaling
    scale = StandardScaler()
    scale.fit(df.drop("Class", axis=1))
    scale_feat = scale.fit_transform(df.drop("Class", axis=1))
    df_feat = pd.DataFrame(scale_feat, columns=df.columns[:-1])

    # Train test split
    x = df_feat
    y = df["Class"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    image_var = tf.feature_column.numeric_column("Image.Var")
    image_skew = tf.feature_column.numeric_column('Image.Skew')
    image_curt = tf.feature_column.numeric_column('Image.Curt')
    entropy =tf.feature_column.numeric_column('Entropy')

    feat_cols = [image_var, image_skew, image_curt, entropy]
    classifier = tf.estimator.DNNClassifier(hidden_units=[10, 20, 10], n_classes=2, feature_columns=feat_cols)
    input_func = tf.estimator.inputs.pandas_input_fn(x=x_train, y=y_train, batch_size=10, shuffle=True)
    classifier.train(input_fn=input_func, steps=500)

    # Model Eval
    pred_func = tf.estimator.inputs.pandas_input_fn(x=x_test,batch_size=len(x_test),shuffle=False)
    note_predictions = list(classifier.predict(input_fn=pred_func))
    final_preds  = [p["class_ids"][0] for p in note_predictions]
    print(classification_report(y_test, final_preds))