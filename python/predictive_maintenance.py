import os
import joblib
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "xgboost_machine_health.pkl")
THINGSPEAK_CHANNEL_ID = os.getenv("THINGSPEAK_CHANNEL_ID", "")
THINGSPEAK_READ_API_KEY = os.getenv("THINGSPEAK_READ_API_KEY", "")
THINGSPEAK_WRITE_API_KEY = os.getenv("THINGSPEAK_WRITE_API_KEY", "")

model = joblib.load(MODEL_PATH)

# Change these field names only if your ThingSpeak channel uses a different mapping.
FIELD_MAP = {
    "Temperature": "field1",
    "Humidity": "field2",
    "Pressure": "field3",
    "Vibration": "field4",
    "Current": "field5",
    "RPM": "field6",
    "Power": "field8",
}

def get_latest_reading():
    url = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds/last.json"
    params = {"api_key": THINGSPEAK_READ_API_KEY}
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def make_features(feed):
    # Build the feature names expected by the saved model.
    # If your model reports different feature names, update this mapping.
    row = {
        "Temperature": float(feed.get(FIELD_MAP["Temperature"]) or 0),
        "Humidity": float(feed.get(FIELD_MAP["Humidity"]) or 0),
        "Pressure": float(feed.get(FIELD_MAP["Pressure"]) or 0),
        "Vibration": float(feed.get(FIELD_MAP["Vibration"]) or 0),
        "Current": float(feed.get(FIELD_MAP["Current"]) or 0),
        "RPM": float(feed.get(FIELD_MAP["RPM"]) or 0),
        "Power": float(feed.get(FIELD_MAP["Power"]) or 0),
    }
    return pd.DataFrame([row])

def predict(feed):
    X = make_features(feed)
    pred = model.predict(X)[0]
    result = str(pred)

    probabilities = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X)[0].tolist()

    return result, probabilities

def write_prediction(prediction):
    if not THINGSPEAK_WRITE_API_KEY:
        print("No ThingSpeak write key configured; prediction was not uploaded.")
        return

    url = "https://api.thingspeak.com/update"
    # Reserve field9 for the text prediction if your channel supports it.
    params = {
        "api_key": THINGSPEAK_WRITE_API_KEY,
        "field9": prediction,
    }
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    print("ThingSpeak update response:", r.text)

if __name__ == "__main__":
    if not THINGSPEAK_CHANNEL_ID or not THINGSPEAK_READ_API_KEY:
        raise SystemExit("Set THINGSPEAK_CHANNEL_ID and THINGSPEAK_READ_API_KEY first.")

    feed = get_latest_reading()
    prediction, probabilities = predict(feed)

    print("Latest reading:", feed)
    print("XGBoost prediction:", prediction)
    print("Probabilities:", probabilities)

    write_prediction(prediction)
