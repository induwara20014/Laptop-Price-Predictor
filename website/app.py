from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import os
import pandas as pd  # Add pandas import for DataFrame

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'predictor.pickle')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Model file not found: {filename}")
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    # Define the exact column names with correct prefixes as used in training
    columns = (['Ram', 'Weight', 'Touchscreen', 'Ips'] +
               ['Company_' + item for item in ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba']] +
               ['TypeName_' + item for item in ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']] +
               ['OpSys_' + item for item in ['Android', 'Chrome OS', 'Linux', 'Mac OS X', 'No OS', 'Windows 10', 'Windows 10 S', 'Windows 7', 'macOS']] +
               ['cpu_name_' + item for item in ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other']] +
               ['gpu_name_' + item for item in ['AMD', 'Intel', 'Nvidia']])
    df = pd.DataFrame([lst], columns=columns)
    pred_value = model.predict(df)
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = None  # No prediction at start

    if request.method == 'POST':
        print("POST request received")  # Debug print
        ram = request.form.get('ram')
        weight = request.form.get('weight')
        company = request.form.get('company')
        typename = request.form.get('typename')
        opsys = request.form.get('opsys')
        cpu = request.form.get('cpuname')
        gpu = request.form.get('gpuname')
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        print(f"Form data: ram={ram}, weight={weight}, company={company}, typename={typename}, opsys={opsys}, cpu={cpu}, gpu={gpu}, touchscreen={touchscreen}, ips={ips}")  # Debug print

        # Check for empty form fields
        if not all([ram, weight, company, typename, opsys, cpu, gpu]):
            return render_template('index.html', error="Please fill all required fields")

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))

        # Maps for input to dummy names
        company_map = {'acer': 'Acer', 'apple': 'Apple', 'asus': 'Asus', 'dell': 'Dell', 'hp': 'HP', 'lenovo': 'Lenovo', 'msi': 'MSI', 'other': 'Other', 'toshiba': 'Toshiba'}
        typename_map = {'2in1convertible': '2 in 1 Convertible', 'gaming': 'Gaming', 'netbook': 'Netbook', 'notebook': 'Notebook', 'ultrabook': 'Ultrabook', 'workstation': 'Workstation'}
        opsys_map = {'linux': 'Linux', 'mac': 'macOS', 'windows': 'Windows 10', 'other': 'No OS'}
        cpu_map = {'amd': 'AMD', 'intelcorei3': 'Intel Core i3', 'intelcorei5': 'Intel Core i5', 'intelcorei7': 'Intel Core i7', 'other': 'Other'}
        gpu_map = {'amd': 'AMD', 'intel': 'Intel', 'nvidia': 'Nvidia'}

        company_dummies = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba']
        typename_dummies = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
        opsys_dummies = ['Android', 'Chrome OS', 'Linux', 'Mac OS X', 'No OS', 'Windows 10', 'Windows 10 S', 'Windows 7', 'macOS']
        cpu_dummies = ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other']
        gpu_dummies = ['AMD', 'Intel', 'Nvidia']

        selected_company = company_map.get(company, company)
        selected_typename = typename_map.get(typename, typename)
        selected_opsys = opsys_map.get(opsys, opsys)
        selected_cpu = cpu_map.get(cpu, cpu)
        selected_gpu = gpu_map.get(gpu, gpu)

        for item in company_dummies:
            feature_list.append(1 if item == selected_company else 0)
        for item in typename_dummies:
            feature_list.append(1 if item == selected_typename else 0)
        for item in opsys_dummies:
            feature_list.append(1 if item == selected_opsys else 0)
        for item in cpu_dummies:
            feature_list.append(1 if item == selected_cpu else 0)
        for item in gpu_dummies:
            feature_list.append(1 if item == selected_gpu else 0)

        print(f"Feature list length: {len(feature_list)}, values: {feature_list}")  # Debug print

        try:
            pred_value = prediction(feature_list)
            print("\nPrediction array (raw output):", pred_value)  # <-- PRINT IN TERMINAL (removed emoji)
            pred_value = np.round(pred_value[0], 2) * 221
            print("Final calculated value:", pred_value, "\n")     # <-- ALSO PRINT IN TERMINAL (removed emoji)
        except Exception as e:
            print(f"Prediction error: {str(e)}")  # Debug print
            return render_template('index.html', error=f"Prediction error: {str(e)}")

        return render_template('index.html', pred_value=pred_value)

    # For GET request — just render the page
    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)
