# src/predict.py which takes two arguments (model and file with data for predict)

# Reads a model from ../model
# Make predictions for each row of argument file
# Save predictions to a new file

import pickle
import sys
import pandas as pd

# Before generate prediction data:
#  python3 get_data.py 2023 08 02 2023 08 03 predict

# get model path and data path:
model_path = sys.argv[-2]
predict_data_path = sys.argv[-1]
prediction_path = "../data/predict-done-2023-08-03.parque"

model = pickle.load(open(model_path,'rb'))
new_input_data = pd.read_parquet(predict_data_path)

print(" Make prediciton ...")
prediction = model.predict(new_input_data)

prediction.to_parquet(prediction_path)