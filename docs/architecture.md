# System Architecture

1. Wokwi simulates the ESP32 sensor environment.
2. Sensor values are sent to ThingSpeak.
3. Python retrieves the latest reading.
4. The saved XGBoost model predicts the machine condition.
5. The prediction can be written back to ThingSpeak.
6. Power BI reads the sensor and prediction fields for visualization.

Data path:

Wokwi → ThingSpeak → Python/XGBoost → ThingSpeak → Power BI
