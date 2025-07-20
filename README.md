🏠 House Price Predictor
Welcome to the House Price Predictor – a beginner-friendly machine learning project that predicts housing prices using Linear Regression trained on the Ames Housing dataset. This project walks through the full ML workflow: from cleaning data to training a model and making predictions through a simple CLI tool.

📊 What This Project Does
Uses the Ames Housing dataset to build a regression model

Preprocesses data (cleaning, handling missing values, encoding)

Trains a Linear Regression model using scikit-learn

Saves the model and feature set using joblib

Lets users predict house prices with a command-line interface

🚀 Key Features
Drops unnecessary and sparse columns

Fills or handles missing data effectively

Uses one-hot encoding for categorical variables

Splits the data into training and testing sets

Evaluates model performance (using RMSE)

Allows user input for predictions via app.py

🧰 Technologies Used
Python 3.13+

pandas for data manipulation

NumPy for numerical operations

scikit-learn for machine learning

joblib for model serialization

🛠️ How to Use It
Clone this repository:

bash
Copy
Edit
git clone https://github.com/Sayak-Ghosh99/house-price-predictor.git
cd house-price-predictor
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Train the model:

bash
Copy
Edit
python train_model.py
Run the prediction app:

bash
Copy
Edit
cd app
python app.py
📁 Folder Structure
graphql
Copy
Edit
house-price-predictor/
├── app/
│   └── app.py                  # CLI app for predictions
├── data/
│   └── AmesHousing.csv         # Dataset (not pushed to GitHub)
├── linear_regression_model.pkl # Trained model
├── model_features.pkl          # Feature names for input
├── train_model.py              # Training script
├── requirements.txt            # Required libraries
└── README.md                   # This file!
💬 Example Output
yaml
Copy
Edit
Model trained successfully!
RMSE on test data: 29101.52

Enter value for Overall Qual: 8
Enter value for Gr Liv Area: 1700
...

💰 Predicted House Price: ₹254200.75
📬 Contact
If you have questions, suggestions, or just want to connect:

GitHub: Sayak Ghosh

Email: ghoshsayak2017@gmail.com
