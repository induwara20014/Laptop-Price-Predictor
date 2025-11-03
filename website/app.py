from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import os

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'predictor.pickle')
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = None  # No prediction at start

    if request.method == 'POST':
        ram = request.form.get('ram')
        weight = request.form.get('weight')
        company = request.form.get('company')
        typename = request.form.get('typename')
        opsys = request.form.get('opsys')
        cpu = request.form.get('cpuname')
        gpu = request.form.get('gpuname')
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        # Check for empty form fields
        if not all([ram, weight, company, typename, opsys, cpu, gpu]):
            return render_template('index.html', error="Please fill all required fields")

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))

        company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
        typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
        opsys_list = ['linux','mac','other','windows']
        cpu_list = ['amd','intelcorei3','intelcorei5','intelcorei7','other']
        gpu_list = ['amd','intel','nvidia']

        # Helper to encode categories
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(company_list, company)
        traverse_list(typename_list, typename)
        traverse_list(opsys_list, opsys)
        traverse_list(cpu_list, cpu)
        traverse_list(gpu_list, gpu)

        try:
            pred_value = prediction(feature_list)
            print("\n✅ Prediction array (raw output):", pred_value)  # <-- PRINT IN TERMINAL
            pred_value = np.round(pred_value[0], 2) * 221
            print("💰 Final calculated value:", pred_value, "\n")     # <-- ALSO PRINT IN TERMINAL
        except Exception as e:
            return render_template('index.html', error=f"Prediction error: {str(e)}")

        return render_template('index.html', pred_value=pred_value)

    # For GET request — just render the page
    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)
