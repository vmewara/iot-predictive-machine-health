IoT Predictive Machine Health Monitoring is an end-to-end predictive maintenance prototype designed to demonstrate how IoT sensor data, cloud data collection, machine learning, and interactive dashboards can be combined to monitor machine conditions and identify potential abnormal operating states.

The project uses an ESP32 simulated in Wokwi to generate machine-related sensor readings such as temperature, humidity, pressure, vibration, and current. These simulated readings are transmitted to ThingSpeak, which acts as the cloud-based data collection layer.

The collected data is then processed using Python, where additional machine parameters such as RPM and power consumption can be derived from the sensor readings. A trained XGBoost machine learning classification model analyzes the machine data and predicts one of three operating conditions:

Normal – machine parameters are within the expected operating range.
Warning – machine parameters indicate a potentially abnormal condition.
Critical – machine parameters indicate a significantly abnormal condition requiring attention.

The trained model is stored using Joblib and integrated into the Python monitoring application. The application retrieves the latest available ThingSpeak data, prepares the input features, and generates the machine-health prediction.

For visualization and monitoring, the project includes a Streamlit dashboard that displays the latest machine readings, calculated parameters, machine health, and the XGBoost prediction. A Power BI dashboard is also used to visualize historical sensor data and trends, including temperature, pressure, vibration, current, machine health, and machine-condition distribution.

System Architecture
Wokwi ESP32 Simulation
        ↓
Simulated Machine Sensors
        ↓
ThingSpeak Cloud
        ↓
Python Data Processing
        ↓
Feature Preparation
        ↓
XGBoost Machine Learning Model
        ↓
Machine Condition Prediction
        ↓
Normal / Warning / Critical
        ↓
Streamlit Dashboard
        ↓
Power BI Visualization
Key Features

IoT Simulation

ESP32-based machine monitoring simulation using Wokwi
Simulated temperature and other machine parameters
Cloud-based data transmission through ThingSpeak

Machine Learning

XGBoost classification model
Three machine condition classes
Model saved as xgboost_machine_health.pkl
Python-based prediction pipeline

Real-Time Monitoring Prototype

Retrieves the latest available ThingSpeak reading
Processes sensor values automatically
Generates machine-health predictions

Streamlit Dashboard

Latest sensor readings
Temperature and humidity
Pressure
Vibration
Current
RPM
Power consumption
Machine health
Predicted machine condition

Power BI Dashboard

Temperature trend
Pressure trend
Vibration trend
Current trend
Machine health monitoring
Machine condition distribution
Date and time filtering
Technologies Used

Programming & Machine Learning

Python
Pandas
NumPy
Scikit-learn
XGBoost
Joblib

IoT & Cloud

ESP32
Wokwi
ThingSpeak

Visualization

Streamlit
Microsoft Power BI

Development & Version Control

Git
GitHub
Machine Learning Prediction

The XGBoost model uses machine-related parameters to classify the current operating condition.

0 → Critical
1 → Normal
2 → Warning

The model receives processed machine parameters and returns the predicted class, which is then converted into a human-readable machine status.

Project Workflow
Simulate machine sensor readings using an ESP32 in Wokwi.
Send the simulated readings to ThingSpeak.
Retrieve the latest available readings using Python.
Prepare the required machine-learning features.
Generate machine-condition predictions using XGBoost.
Display the prediction and sensor values through Streamlit.
Visualize machine readings and historical trends using Power BI.
Use the dashboards to monitor machine health and identify abnormal operating conditions.
Repository Structure
iot-predictive-machine-health/
│
├── docs/
│   ├── architecture.md
│   └── model_notes.md
│
├── ml/
│   └── README.md
│
├── powerbi/
│   └── README.md
│
├── python/
│   └── predictive_maintenance.py
│
├── xgboost_machine_health.pkl
├── requirements.txt
├── README.md
└── .gitignore
Project Purpose

The main purpose of this project is to demonstrate a complete IoT → Cloud → Machine Learning → Dashboard workflow for predictive machine-health monitoring. It brings together multiple technologies into a single prototype rather than treating IoT, machine learning, and visualization as separate demonstrations.

Important Note

This project uses simulated sensor data generated through Wokwi and is intended for educational, academic, and prototype demonstration purposes. The system does not currently use sensors connected to a physical industrial machine, so the predictions should not be interpreted as validated predictions for real industrial equipment.

Author

S.Vishal

Vishal Mewara
BCA Data Science
SRM Institute of Science and Technology
