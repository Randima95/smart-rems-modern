from pathlib import Path
import json
from .data import generate_synthetic_hourly_data
from .forecast import train_forecaster
from .rl import q_learning_schedule
from .controller import dispatch_loads

def main():
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "data"
    results_dir = root / "results"

    data_dir.mkdir(exist_ok=True)
    results_dir.mkdir(exist_ok=True)

    df = generate_synthetic_hourly_data()
    df.to_csv(data_dir / "synthetic_rems_hourly.csv", index=False)

    _, metrics = train_forecaster(df)
    (results_dir / "forecast_metrics.json").write_text(json.dumps(metrics, indent=2))

    schedule = q_learning_schedule(df)
    preview = df.head(48).copy()
    preview["chosen_action"] = [x[0] for x in schedule[:48]]
    preview["battery_soc_kwh"] = [x[1] for x in schedule[:48]]
    preview.to_csv(results_dir / "dispatch_preview.csv", index=False)

    dispatch = dispatch_loads(
        [
            ("refrigerator", 0.25, 1),
            ("lights", 0.3, 2),
            ("fans", 0.6, 3),
            ("water_heater", 1.2, 4),
            ("ac", 1.8, 5),
        ],
        2.5,
        False,
    )

    (results_dir / "example_dispatch.json").write_text(json.dumps(dispatch, indent=2))

if __name__ == "__main__":
    main()
