
# Project Title

**Water Quality Prediction Using XGBoost** is an AI-powered web application that predicts whether water is safe to drink or not, based on nine critical chemical parameters. Built using a machine learning pipeline with XGBoost Classifier, this system helps identify potable water samples in real-time. The model is trained on a cleaned and balanced dataset, and the web interface is implemented using Flask, with a responsive HTML/CSS frontend for user interaction.

This project is designed for public health monitoring, environmental awareness, and as a demonstration of applied machine learning in water safety analysis. It is lightweight, offline-compatible, and easy to deploy.

---
## 🖥️ Features

- Accepts 9 chemical parameters as input
- Predicts potability using XGBoost Classifier
- Clean Flask web interface with instant result
- Model trained with GridSearchCV tuning
- Displays 💧 "Safe" or 🚫 "Not Safe" feedback

---





## 📊 Input Features

| Feature            | Description                                |
|--------------------|--------------------------------------------|
| `ph`               | Acidity/alkalinity of water                |
| `hardness`         | Calcium and magnesium concentration        |
| `solids`           | Total dissolved solids (TDS)               |
| `chloramines`      | Disinfectant used in treatment             |
| `sulfate`          | Sulfate ion level                          |
| `conductivity`     | Electrical conductivity                    |
| `organic_carbon`   | Organic content                            |
| `trihalomethanes`  | Chlorination by-products                   |
| `turbidity`        | Clarity or cloudiness of water             |

---
## 🚀 Getting Started

Clone the project

```bash
  git clone https://github.com/tamilamudan/Water-Quality-Prediction-Using-XGBoost.git
```

Go to the project directory

```bash
  cd Water-Quality-Prediction-Using-XGBoost

```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the App

```bash
python app.py
```



---
## 📦 Dependencies

```txt
flask==3.1.1  
numpy==2.1.3  
pandas==2.2.3  
scikit-learn==1.6.1  
matplotlib==3.10.3  
xgboost==3.0.2  
notebook==7.2.0  
```
---
## 📁 Project Structure
``` markdown
├── app.py                          # Flask backend
├── Wqp_model.pkl                   # Trained XGBoost model
├── Water_quality_prediction.ipynb  # Jupyter Notebook (model training)
├── clean_balanced_water_potability.csv  # Dataset
├── requirements.txt                # Dependencies
├── templates/
│   └── index.html                  # Frontend UI
└── static/
    └── style.css                   # Styling


```
## 🧠 Model Info

- Model: XGBClassifier with GridSearchCV

- Scaled features using StandardScaler

- Trained on balanced dataset with 9 inputs

- Saved as Wqp_model.pkl via pickle

## 📸 Screenshots
 ### 🧾 Form UI
<img width="1866" height="903" alt="image" src="https://github.com/user-attachments/assets/fcdc9bfe-f863-4e89-8f7e-832a78ab0b04" />

### ✅ Prediction Result
##### Safe To Drink
<img width="1280" height="622" alt="image" src="https://github.com/user-attachments/assets/d05c9923-5c2c-4e57-8402-ae1b920397ca" />

##### Not Safe To Drink
<img width="1280" height="621" alt="image" src="https://github.com/user-attachments/assets/da35bea6-3785-4bab-aa90-589c1c5b8feb" />

## 👤 Author
  #### **Tamil Amudan K.S.R**
   - [Github](https://github.com/tamilamudan)

   - [Linkedin](https://www.linkedin.com/in/tamil-amudan-k-s-r/)

