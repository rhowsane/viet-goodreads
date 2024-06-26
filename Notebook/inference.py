import sys; print(f"python {sys.version}")

import numpy as np
import pandas as pd
import joblib

from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, mean_absolute_error

def inference():

    test = "test_df.csv"
    model_rf = "random_forest.joblib"

    test_df = pd.read_csv(test)
    test_df.set_index("Unnamed: 0", inplace= True)

    print(f"Dimensions of the test dataframe: {test_df.shape}")

    test_features = test_df.drop(columns=['average_rating'])
    print(f"Test features names: {test_features.columns.tolist()}")

    model = joblib.load(model_rf)
    predictions = model.predict(test_features)

    print(f"Random forest metrics:")

    mse = mean_squared_error(test_df['average_rating'], predictions)
    print(f"Mean Squared Error of Random Forest Regressor: {mse:.2f}")

    mae = mean_absolute_error(test_df['average_rating'], predictions)
    print(f"Mean Absolute Error: {mae:.2f}")

    r2 = r2_score(test_df['average_rating'], predictions)
    print(f"R-squared: {r2:.2f}")

if __name__ == '__main__':
    inference()