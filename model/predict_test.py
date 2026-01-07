import pickle
import numpy as np

with open('predictor.pickle', 'rb') as file:
    model = pickle.load(file)

print("Number of features expected:", model.n_features_in_)
print("Feature names:", model.feature_names_in_)

# Sample input: Apple Ultrabook, 8GB RAM, 1.3kg, touchscreen=yes, IPS=yes, macOS, Intel Core i5, Intel GPU
input_features = [8, 1.3, 1, 1,  # Ram, Weight, Touchscreen, Ips
                  0,1,0,0,0,0,0,0,0,  # Company: Apple
                  0,0,0,0,1,0,  # TypeName: Ultrabook
                  0,0,0,0,0,0,0,0,1,  # OpSys: macOS
                  0,0,1,0,0,  # cpu_name: Intel Core i5
                  0,1,0]  # gpu_name: Intel

pred = model.predict([input_features])
final_value = np.round(pred[0], 2) * 221
print(f"Predicted laptop price: {final_value} euros")