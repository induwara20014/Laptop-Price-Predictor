# Laptop Price Predictor

A Flask web application that predicts laptop prices based on user-specified specifications using a machine learning model.

## Features

- Predict laptop prices based on RAM, weight, company, type, operating system, CPU, GPU, touchscreen, and IPS display.
- Simple web interface built with Flask and HTML templates.

## Setup Instructions

1. **Prerequisites**:
   - Python 3.7 or higher installed on your system.
   - Git (optional, for cloning the repository).

2. **Clone or Download the Repository**:
   - Download the project files to your local machine.

3. **Navigate to the Project Directory**:
   - Open a terminal and change to the `website` folder:
     ```
     cd path/to/Laptop-Price-Predictor/website
     ```

4. **Activate the Virtual Environment**:
   - The project includes a pre-configured virtual environment in the `env/` folder.
   - Activate it using:
     - On Windows: `env\Scripts\activate`
     - On macOS/Linux: `source env/bin/activate`

5. **Install Dependencies**:
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```
   - Note: If `pandas` is not included in `requirements.txt`, install it separately:
     ```
     pip install pandas
     ```

6. **Ensure Model File Exists**:
   - The application requires a trained model file located at `../model/predictor.pickle`.
   - Verify that this file exists in the parent directory's `model/` folder.

7. **Run the Application**:
   - Start the Flask development server:
     ```
     python app.py
     ```
   - The application will run in debug mode and be accessible at `http://127.0.0.1:5000/`.

8. **Access the Web Interface**:
   - Open your web browser and navigate to `http://127.0.0.1:5000/`.
   - Fill in the laptop specifications in the form and submit to receive a price prediction.

## Usage

- Select or enter the laptop specifications (RAM, weight, company, etc.).
- Check the appropriate checkboxes for touchscreen and IPS display if applicable.
- Click "Predict Price" to get an estimated price.
- The prediction is displayed on the same page.

## Project Structure

- `app.py`: Main Flask application file containing the prediction logic.
- `requirements.txt`: List of Python dependencies.
- `templates/index.html`: HTML template for the web interface.
- `static/style.css`: CSS file for styling the web page.
- `env/`: Virtual environment folder.
- `../model/`: Directory containing the trained machine learning model (`predictor.pickle`).

## Troubleshooting

- **Model File Not Found**: Ensure the `predictor.pickle` file is present in the `../model/` directory.
- **Import Errors**: Make sure all dependencies are installed and the virtual environment is activated.
- **Port Issues**: If port 5000 is in use, modify the `app.run()` call in `app.py` to use a different port.

## Contributing

Feel free to contribute by submitting issues or pull requests to improve the application.

## License

This project is for educational purposes. Check individual licenses for dependencies.