
import sys

# Data
import pandas as pd

# Export
import pickle

class ModelPredictor():

    def __init__(self):
        self.Y_prediction = None
        self.model = None
        self.one_hot_enc = None
    
    def read_model(self, model_pickle_path: str) -> None:
        """
        Read a model.pkl file and saved in a attribute.
        """
        file = open(model_pickle_path, "rb")
        self.model = pickle.load(file)
        file.close()

    def save_prediction(self, prediction_path):
        self.Y_prediction = pd.DataFrame({'Prediction': self.Y_prediction})
        self.Y_prediction.to_parquet(prediction_path)

    def get_y_prediction(self) -> pd.Series:
        """
        Return prediction made by model.
        """
        if self.Y_prediction is None:
            raise ValueError("Y_prediction has not been prepared. Call 'predict' first.")
        return self.Y_prediction

    def predict(self, X_test: pd.DataFrame) -> None:
        """
        Predicts the target values for the test set.
        """
        self.Y_prediction = self.model.predict(X_test)

if __name__ == '__main__':
    
    if len(sys.argv) != 3 :
        print(f" [ERROR] Arguments recived from command line : {sys.argv}")
        raise ValueError(" [ USAGE ]: python3 predictor.py <path-to-model> <path-new-generated-data>")

    data_predict_path = sys.argv[-1]
    model_path = sys.argv[-2]

    # Take arguments from console
    print("\n    [INFO] Reading new data ...")
    df_predict = pd.read_parquet(data_predict_path)

    # Instantiate processor
    print("\n    [INFO] Creating ModelPredictor() ...")
    predictor = ModelPredictor()

    # Read model
    print("\n    [INFO] Read model ...")
    predictor.read_model(model_pickle_path = model_path)

    # Make prediction
    print("\n    [INFO] Make prediction ...")
    predictor.predict(X_test = df_predict)

    print("\n    [INFO] Predict value : \n")
    Y_prediction = predictor.get_y_prediction()
    print(f"{Y_prediction} \n")

    # Save prediction
    prediction_date = data_predict_path.split('predict')[1][1:].split('.')[0]
    prediction_path = "../data/predict-done-" + prediction_date + ".parquet"
    predictor.save_prediction(prediction_path=prediction_path)
