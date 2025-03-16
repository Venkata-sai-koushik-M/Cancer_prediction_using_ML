# 🏥 Cancer Prediction using Machine Learning

This project uses **Machine Learning (Random Forest Classifier)** to predict cancer type based on user symptoms.  
It can detect **Lung Cancer, Cervical Cancer, Breast Cancer, Thyroid Cancer, and Blood Cancer** based on symptoms.  

---

## 📌 Features
✅ User enters symptoms to predict possible cancer type  
✅ Machine Learning model trained on synthetic dataset  
✅ Supports **Lung, Cervical, Breast, Thyroid, Blood Cancers**  
✅ **99% accuracy** on test data  

---

## 📂 Dataset & Model
🔹 **Dataset:** `cancer_symptoms_dataset.csv`  
🔹 **Trained Model:** `cancer_prediction_model.pkl`  

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Venkata-sai-koushik-M/cancer_prediction_using_ML.git
cd cancer-prediction-ml
```

### **2️⃣ Install Dependencies**
```bash
pip install pandas scikit-learn joblib
        [0r]
pip install -r requirements.txt

```

### **3️⃣ Run the Jupyter Notebook**
```bash
jupyter notebook
```
Open `Cancer_Prediction.ipynb` and run all the cells.

---
---
## 🚀 How to Run in VS Code?

### 1️⃣ Download cancer_prediction.py and cancer_prediction_model.pkl

### 2️⃣ Install dependencies (if not installed)
```sh
pip install joblib numpy
```
3️⃣ Run the script
```sh
python cancer_prediction.py
```
4️⃣ Enter symptoms (1 for Yes, 0 for No) and get predicted cancer type


## 🔍 How to Use the Model?

### **Run Python Script**
```bash
python cancer_prediction.py
```
### **Example User Input**
```
Do you have chronic cough? (1 for Yes, 0 for No): 1
Do you have weight loss? (1 for Yes, 0 for No): 1
Do you have fatigue? (1 for Yes, 0 for No): 0
...
🔍 Predicted Cancer Type: Lung Cancer
```

---

## 📌 Future Enhancements
✅ Add **Web App** using Flask or Streamlit  
✅ Improve dataset with real medical records  
✅ Integrate with **X-ray/CT Scan AI models**  

---

## 📜 License
This project is open-source. Feel free to use and improve it. 🚀  

---

## 💡 Need Help?
If you have any issues, feel free to create an **Issue** on GitHub or contact me. 

## Authors
1-[M.Venkata sai koushik][https://github.com/Venkata-sai-koushik-M?tab=repositories]

2-[R.L.Sriyutha][https://github.com/Sriyutha-R-L]
