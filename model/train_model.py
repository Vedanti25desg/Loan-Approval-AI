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
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

DATA_PATH = "dataset/loan_approval_data.csv"
MODEL_PATH = "creditwise_pipeline.joblib"
RANDOM_STATE = 42
TEST_SIZE = 0.2

def main():
    # 1) Load data
    df = pd.read_csv(DATA_PATH)

    df = df.dropna(subset=["Loan_Approved"]).copy()

    # 2) Basic validation
    df["Loan_Approved"] = df["Loan_Approved"].astype(str).str.strip()
    df["Loan_Approved"] = df["Loan_Approved"].replace({
        "YES": "Yes", "yes": "Yes", "Approved": "Yes", "approved": "Yes", "1": "Yes",
        "NO": "No", "no": "No", "Rejected": "No", "rejected": "No", "0": "No",
    })

    # 3) Target + drop ID
    y = df["Loan_Approved"]
    X = df.drop(columns=["Loan_Approved", "Applicant_ID"], errors="ignore")

    # 4) Define categorical + numerical columns
    cat_cols = [
        "Employment_Status", "Marital_Status", "Loan_Purpose",
        "Property_Area", "Gender", "Employer_Category", "Education_Level"
    ]
    num_cols = [c for c in X.columns if c not in cat_cols]

    # 5) Preprocessing pipelines
    numeric_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(drop="first", handle_unknown="ignore")),
    ])

    preprocess = ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, num_cols),
            ("cat", categorical_pipe, cat_cols),
        ],
        remainder="drop",
    )

    # 6) Model (simple + strong baseline)
    clf = Pipeline(steps=[
        ("preprocess", preprocess),
        ("model", LogisticRegression(max_iter=2000))
    ])

    # 7) Train/test split (stratify helps if classes are imbalanced)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    # 8) Train + evaluate
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    print("\n=== Evaluation on Test Set ===")
    print(classification_report(y_test, preds))

    # 9) Save the full pipeline (preprocess + model)
    joblib.dump(clf, MODEL_PATH)
    print(f"\nSaved model pipeline to: {MODEL_PATH}")

if __name__ == "__main__":
    main()



