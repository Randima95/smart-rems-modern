import numpy as np
import pandas as pd

def generate_synthetic_hourly_data(seed=42):
    rng = np.random.default_rng(seed)
    t = pd.date_range("2025-01-01", periods=24 * 30, freq="h")
    h = t.hour
    daylight = np.clip(np.sin(np.pi * (h - 6) / 12), 0, None)
    irradiance = 850 * daylight * np.clip(rng.normal(0.9, 0.12, len(t)), 0.4, 1.1)
    temperature = 28 + 3 * np.sin(2 * np.pi * (h - 8) / 24) + rng.normal(0, 1, len(t))
    pv = np.clip(irradiance * 0.0055, 0, None)
    demand = np.clip(
        1.3 + ((h >= 18) & (h <= 23)) * 1.5 + ((h >= 8) & (h <= 17)) * 0.6 + rng.normal(0, 0.12, len(t)),
        0.5,
        None,
    )
    return pd.DataFrame(
        {
            "timestamp": t,
            "hour": h,
            "ambient_temperature_c": temperature,
            "irradiance_wm2": irradiance,
            "pv_generation_kwh": pv,
            "demand_kwh": demand,
        }
    )
