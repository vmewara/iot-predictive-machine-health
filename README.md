# IoT Predictive Machine Health Monitoring

A student portfolio project that demonstrates simulated IoT machine monitoring and predictive maintenance.

## Architecture

Wokwi ESP32 → ThingSpeak → Python/XGBoost → prediction → ThingSpeak → Power BI

## Technologies
- Wokwi / ESP32
- ThingSpeak
- Python
- XGBoost
- scikit-learn
- pandas / NumPy
- Power BI
- GitHub

## Sensor fields
- Temperature (°C)
- Humidity (%)
- Pressure (kPa)
- Vibration
- Current (A)
- RPM
- Power (W)
- Machine Health (%)
- Prediction (Normal / Warning / Critical)

## Important project note
The sensor environment is simulated in Wokwi. This project demonstrates the software/data pipeline and is not a claim of validation on a physical industrial machine.

## Model
The trained model is supplied as `xgboost_machine_health.pkl`. Keep the Python/scikit-learn versions in `requirements.txt` consistent with the environment used to create the model.

Model performance numbers should only be added from the actual model-performance report or evaluation output.

## Project structure
```text
wokwi/
python/
ml/
powerbi/
docs/
data/
```

## Setup
1. Create a Python virtual environment.
2. Install `requirements.txt`.
3. Put the ThingSpeak Read/Write API keys in environment variables or a local `.env` file. Never commit API keys.
4. Run `python python/predictive_maintenance.py`.
5. Import the ThingSpeak data into Power BI.
6. Add the prediction field to the Power BI report.
