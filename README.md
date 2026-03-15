# 🚗 Predictive Vehicle Maintenance System

A **Machine Learning–based Predictive Maintenance System** designed to detect potential vehicle failures before they occur.  
This project analyzes **vehicle sensor data** and predicts whether the vehicle condition is **Safe, Warning, or Critical**, enabling proactive maintenance and reducing unexpected breakdowns.

The system includes an **interactive Streamlit dashboard** where users can input vehicle parameters and instantly receive a health prediction.

---

# 📌 Project Overview

Predictive maintenance is an important application of machine learning in the **automotive and industrial sectors**.  
Instead of waiting for components to fail, predictive systems analyze sensor data to identify patterns that indicate possible faults.

In this project:

- A **Gradient Boosting Classifier** is used as the machine learning model.
- The model is trained on a **dataset containing 100,000 rows and 7 features**.
- Vehicle conditions are categorized into **three maintenance levels** using threshold configurations.

This helps simulate a **real-world predictive monitoring system**.

---

# ✨ Key Features

- **Machine Learning Prediction**  
  Uses a **Gradient Boosting Classifier** to predict vehicle condition.

- **Interactive Streamlit UI**  
  A simple and user-friendly interface for entering sensor values and viewing predictions.

- **Three-Level Maintenance Classification**

  - 🟢 **Safe** – Vehicle operating normally  
  - 🟡 **Warning** – Possible issue detected  
  - 🔴 **Critical** – Immediate maintenance required  

- **JSON-Based Threshold Configuration**

  The system uses configuration files to determine safety levels:

  - `safe.json`
  - `warning.json`
  - `critical.json`
  - `thresholds.json`

  This allows easy adjustment of threshold values without modifying the main code.

---

# 🧠 Machine Learning Model

The project uses a **Gradient Boosting Classifier**, an ensemble learning algorithm that builds multiple decision trees sequentially to improve prediction accuracy.

### Why Gradient Boosting?

- High predictive performance
- Handles complex patterns in data
- Works well with structured datasets
- Reduces overfitting through boosting techniques

---

# 📊 Dataset

The dataset used in this project contains:

- **100,000 rows**
- **7 columns (features)** related to vehicle operating conditions.

These features simulate **vehicle sensor readings** used to determine potential failure conditions.

---

# 🖥️ Streamlit Interface

The system uses **Streamlit** to build an interactive dashboard where users can:

- Input vehicle sensor values
- Run the predictive model
- Instantly view the vehicle health status

This makes the project easy to test and demonstrate.

---

# 📁 Project Structure

```
predictive-vehicle-maintenance/
│
├── app/
│   └── predictive_maintenance_system.py
│
├── config/
│   ├── safe.json
│   ├── warning.json
│   ├── critical.json
│   └── thresholds.json
│
├── data/
│   └── vehicle_predictive_maintenance_dataset.xlsx
│
├── notebooks/
│   ├── New_model_development.ipynb
│   └── model_selection.ipynb
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Folder Description

| Folder | Description |
|------|------|
| **app/** | Contains the Streamlit application |
| **config/** | JSON files storing threshold configurations |
| **data/** | Dataset used for model training |
| **notebooks/** | Jupyter notebooks for model development and experimentation |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/predictive-vehicle-maintenance.git
```

Navigate to the project directory:

```bash
cd predictive-vehicle-maintenance
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Application

Start the Streamlit app:

```bash
streamlit run app/predictive_maintenance_system.py
```

The dashboard will open in your browser.

---

# 🎯 Applications

This project can be used in:

- Smart vehicle monitoring systems
- Fleet management platforms
- Industrial equipment monitoring
- IoT-based predictive maintenance solutions

---

# 🔮 Future Improvements

- Integration with **real-time IoT sensor data**
- Deployment using **Docker or cloud platforms**
- Addition of **real-time alerts and notifications**
- Advanced **model optimization and feature engineering**

---

# 🛠 Tech Stack

- **Python**
- **Machine Learning (Scikit-learn)**
- **Gradient Boosting Classifier**
- **Streamlit**
- **Pandas**
- **NumPy**
- **JSON configuration**

---

# 📜 License

This project is licensed under the **MIT License**.
