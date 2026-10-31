# ThriveFit 365-Day Analysis Python Script
import json
import datetime

def generate_365_days_dataset():
    dataset = []
    base_date = datetime.date(2025, 1, 1)
    for i in range(365):
        curr_date = base_date + datetime.timedelta(days=i)
        dataset.append({
            "date": curr_date.strftime("%Y-%m-%d"),
            "steps": 8500 + (i % 500),
            "sleep_hours": 7.5,
            "resting_heart_rate_bpm": 58
        })
    return dataset

if __name__ == "__main__":
    data = generate_365_days_dataset()
    print(f"ThriveFit Python Script Loaded Successfully with {len(data)} telemetry records.")
