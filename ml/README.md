# ML model

The trained XGBoost model is stored at the project root as:

`xgboost_machine_health.pkl`

The prediction script loads this file and applies it to the latest ThingSpeak reading.

Do not change the model file unless you intentionally retrain and evaluate a new model.
