import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 1️⃣ Load Dataset
data = pd.read_csv("../dataset/train_data.csv")

print("Dataset Loaded Successfully")
print("Shape:", data.shape)

# 2️⃣ Drop Loan_ID (not useful for prediction)
if "Loan_ID" in data.columns:
    data = data.drop("Loan_ID", axis=1)

# 3️⃣ Handle Missing Values
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].median())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].median())
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].mode()[0])

# 4️⃣ Fix Dependents Column (convert 3+ to 3)
data["Dependents"] = data["Dependents"].astype(str)
data["Dependents"] = data["Dependents"].replace("3+", "3")
data["Dependents"] = data["Dependents"].astype(int)

# Remove any remaining missing values
data = data.fillna(0)

# 5️⃣ Encode Categorical Columns
label_encoder = LabelEncoder()

categorical_columns = [
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# 6️⃣ Create New Features (for better model)
data["Total_Income"] = data["ApplicantIncome"] + data["CoapplicantIncome"]
data["EMI_Ratio"] = data["LoanAmount"] / data["Total_Income"]

# 7️⃣ Define X and y
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

# 8️⃣ Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 9️⃣ Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔟 Check Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# 1️⃣1️⃣ Save Model
pickle.dump(model, open("loan_model.pkl", "wb"))

print("Model trained and saved successfully!")