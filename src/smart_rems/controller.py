def dispatch_loads(loads, battery_available_kwh, grid_available=True):
    remaining = battery_available_kwh
    battery = []
    grid = []
    unsupplied = []

    for name, demand, priority in sorted(loads, key=lambda x: x[2]):
        if remaining >= demand:
            battery.append(name)
            remaining -= demand
        elif grid_available:
            grid.append(name)
        else:
            unsupplied.append(name)

    return {
        "battery": battery,
        "grid": grid,
        "unsupplied": unsupplied,
        "remaining_battery_kwh": round(remaining, 3),
    }
