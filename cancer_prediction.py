import joblib
import numpy as np

# Load the trained model
model = joblib.load("cancer_prediction_model.pkl")

# Function to take user input for symptoms
def get_user_symptoms():
    symptoms_list = [
        "chronic cough", "chest pain", "weight loss", "shortness of breath", "fatigue",
        "pelvic pain", "abnormal bleeding", "pain during intercourse", "breast lump",
        "nipple discharge", "breast pain", "skin dimpling", "neck swelling", "hoarseness",
        "difficulty swallowing", "fever", "frequent infections", "bruising", "swollen lymph nodes"
    ]

    user_symptoms = []
    print("\n🔹 Enter 1 if you have the symptom, 0 if you do not.")
    
    for symptom in symptoms_list:
        while True:
            try:
                value = int(input(f"Do you have {symptom}? (1 for Yes, 0 for No): "))
                if value in [0, 1]:
                    user_symptoms.append(value)
                    break
                else:
                    print("❌ Invalid input! Please enter 1 or 0.")
            except ValueError:
                print("❌ Invalid input! Please enter a number (1 or 0).")

    return np.array(user_symptoms).reshape(1, -1)

# Get user symptoms dynamically
user_symptoms = get_user_symptoms()

# Predict cancer type based on user input
predicted_cancer = model.predict(user_symptoms)
print("\n🔍 Predicted Cancer Type:", predicted_cancer[0])
