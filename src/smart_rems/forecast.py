from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_forecaster(df):
    X = df[["hour", "ambient_temperature_c", "irradiance_wm2"]]
    y = df["pv_generation_kwh"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = Pipeline(
        [
            ("scale", StandardScaler()),
            ("mlp", MLPRegressor(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)),
        ]
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        "rmse": float(mean_squared_error(y_test, preds) ** 0.5),
        "mae": float(mean_absolute_error(y_test, preds)),
        "r2": float(r2_score(y_test, preds)),
    }

    return model, metrics
