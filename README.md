# Smart REMS Modernized

Smart REMS Modernized is a machine learning and reinforcement learning project developed from my undergraduate research on smart residential energy management systems for smart-grid-ready buildings.

## Overview

This project combines solar PV forecasting, battery optimization, and priority-based load dispatch in a modular Python codebase. It simulates how a residence or small building can reduce grid dependency and electricity cost by coordinating rooftop solar, battery storage, and appliance priority rules.

## Core components

- Solar PV forecasting using a neural-network-based regression pipeline
- Battery scheduling using reinforcement learning
- Priority-based load shifting between battery and grid
- Synthetic hourly data generation for reproducible simulation
- Modular Python package design for clean experimentation and extension

## Technical stack

- Python
- NumPy
- Pandas
- scikit-learn

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
python -m src.smart_rems.run_pipeline
```

## Resume line

Built a smart residential energy management system in Python using solar forecasting, reinforcement-learning-based battery scheduling, and priority-based load dispatch.
