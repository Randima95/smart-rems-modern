import numpy as np

def q_learning_schedule(df, episodes=50, seed=42):
    rng = np.random.default_rng(seed)
    actions = np.array(["charge", "discharge", "idle"])
    choices = []
    soc = 10.0

    for _, row in df.iterrows():
        net = row.pv_generation_kwh - row.demand_kwh

        if net > 0.4:
            action = "charge"
        elif net < -0.8 and soc > 2:
            action = "discharge"
        else:
            action = "idle"

        soc = np.clip(
            soc + (min(net, 4) if action == "charge" else -min(-net, 4) if action == "discharge" else 0),
            2,
            20,
        )

        choices.append((action, float(soc)))

    return choices
