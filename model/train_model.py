# Train the Ml model

# ✅ Goal of train_model.py
# The purpose of this code was to:
# Load dataset (train_data.csv)
# Clean the data (handle missing values)
# Convert text to numbers (machine learning needs numbers)
# Train the AI model
# Check accuracy
# Save the trained model (loan_model.pkl)




import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("../dataset/train_data.csv")

print("Dataset loaded successfully")
print("Dataset Shape:", data.shape)

# Remove Loan_ID column
if "Loan_ID" in data.columns:
    data = data.drop("Loan_ID", axis=1)

# Handle Missing Values
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])

data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].median())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].median())
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].mode()[0])

# Fix Dependents column (convert 3+ → 3)
data["Dependents"] = data["Dependents"].replace("3+", 3)
data["Dependents"] = data["Dependents"].astype(int)

# Encode Categorical Data
label_encoder = LabelEncoder()

columns = ["Gender","Married","Education","Self_Employed","Property_Area","Loan_Status"]

for col in columns:
    data[col] = label_encoder.fit_transform(data[col])

# Split Data
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save Model
pickle.dump(model, open("loan_model.pkl", "wb"))

print("Model saved as loan_model.pkl")