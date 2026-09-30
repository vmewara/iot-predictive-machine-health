# Power BI

Recommended report flow:

ThingSpeak data
→ Power BI `feeds` table
→ DateTime
→ latest-value measures
→ sensor trend charts
→ XGBoost prediction

Recommended visuals:
- Latest Date & Time
- Temperature
- Humidity
- Pressure
- Current
- Machine Health
- Temperature Trend
- Pressure Trend
- Current Trend
- Machine Condition
- XGBoost Machine Prediction

If Date and Time are separate:

```DAX
DateTime = feeds[Date] + feeds[Time]
```

Latest timestamp:

```DAX
Latest Date Time = MAX(feeds[DateTime])
```

Example latest-value measure:

```DAX
Latest Temperature =
VAR LatestTime = MAX(feeds[DateTime])
RETURN
    CALCULATE(
        MAX(feeds[Temperature]),
        feeds[DateTime] = LatestTime
    )
```
