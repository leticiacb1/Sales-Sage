from sklearn.ensemble import RandomForestRegressor

import sys
import pickle

n_estimators = 100
random_state = 195

out_type = sys.argv[-1]

print(out_type)
print(len(sys.argv))

if len(sys.argv) != 2 :
    print(" [ USAGE ]: python3 train.py <path-train-data>")


model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
model.fit(X_train, y_train)

# Save the model
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
