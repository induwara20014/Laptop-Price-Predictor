# Laptop Price Predictor

This project is a machine learning based web application that estimates the price of a laptop from its specifications. It uses a trained regression model together with a Flask web interface so users can enter laptop details and get a predicted price instantly.

## Project Idea

The application is built around a simple concept:

1. Collect laptop specifications such as RAM, weight, company, type, operating system, CPU, GPU, touchscreen, and IPS display.
2. Convert the selected values into model-ready features.
3. Load the trained prediction model from a pickle file.
4. Predict the laptop price and show the result on the web page.

## Features

- Predict laptop prices from common hardware and display specifications.
- Web UI built with Flask and HTML templates.
- Supports categorical inputs like company, laptop type, OS, CPU, and GPU.
- Uses checkbox inputs for touchscreen and IPS display.
- Keeps the prediction result on the same page after submission.

## Tech Stack

- Python
- Flask
- pandas
- NumPy
- scikit-learn
- HTML and CSS

## Project Structure

```text
Laptop-Price-Predictor/
├── model/
│   ├── laptop_price .csv
│   ├── model building.ipynb
│   ├── model building.py
│   ├── model_building_clean.py
│   └── predictor.pickle
├── website/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
└── requirements.txt
```

## How It Works

The model is trained using laptop dataset features and target price. During training, the data is cleaned, categorical values are encoded, and a regression model is fitted. The Flask app then loads the saved model and transforms user input into the same feature format used during training.

The prediction flow in the web app is:

1. User submits the form in [website/app.py](website/app.py).
2. The form values are mapped to the training feature layout.
3. The saved model file `model/predictor.pickle` is loaded.
4. The model returns the predicted price.
5. The result is displayed in the browser.

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Laptop-Price-Predictor
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Web App

1. Make sure the trained model file exists at `model/predictor.pickle`.
2. Open the `website` folder.
3. Run the Flask app:

```bash
python app.py
```

4. Open the local server in your browser, usually at:

```text
http://127.0.0.1:5000/
```

## Training the Model

If you want to rebuild the model from scratch, use the scripts inside the `model/` folder. The notebook and Python scripts contain the preprocessing, feature engineering, and model training steps used to generate the pickle file.

## Input Fields

The web form accepts the following values:

- RAM
- Weight
- Company
- Type Name
- Operating System
- CPU name
- GPU name
- Touchscreen
- IPS display

## Notes

- The Flask app expects the trained model file to be available before prediction can run.
- The project includes local virtual environment folders in the workspace, but they are not required if you create your own environment.
- Some file names in the `model/` folder contain spaces, so be careful when opening them from the terminal.

## License

This project is intended for learning and demonstration purposes.
