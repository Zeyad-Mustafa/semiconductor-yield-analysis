# src/data_loader.py

import pandas as pd
import numpy as np
import os

def generate_sample_data(num_wafers=100):
    np.random.seed(42)
    data = []

    for i in range(num_wafers):
        wafer_id = f"W{i+1:04}"
        yield_pct = np.clip(np.random.normal(loc=92, scale=5), 70, 100)
        temp = np.random.normal(450, 10)
        pressure = np.random.normal(1.0, 0.05)
        defect_count = int(np.clip(100 - yield_pct, 0, 30))

        for _ in range(defect_count):
            x = np.random.randint(0, 50)
            y = np.random.randint(0, 50)
            defect_type = np.random.choice(['scratch', 'particle', 'pattern'])
            data.append([wafer_id, x, y, defect_type, yield_pct, temp, pressure])

    df = pd.DataFrame(data, columns=["wafer_id", "x", "y", "defect_type", "yield_pct", "temp", "pressure"])

    # Create the 'data/' directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/sample_wafer_data.csv", index=False)
    print("✅ sample_wafer_data.csv saved in /data")

if __name__ == "__main__":
    generate_sample_data()

