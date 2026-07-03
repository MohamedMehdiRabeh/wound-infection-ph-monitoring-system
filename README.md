# Wound Infection pH Monitoring System

## Overview

This project simulates a biomedical wound monitoring system that analyzes pH changes over time to detect potential infection progression.

It transforms raw time-series pH data into clinically interpretable states using a rule-based model:
- Healthy
- Risk
- Infected

The system produces:
- Time-series visualization of wound pH progression
- Automated classification of wound state
- Clinical-style summary report

---

## Problem Statement

Wound infections often develop gradually and may not be immediately visible through external observation.

pH is a known biochemical indicator of wound status:
- Healthy wounds are typically slightly acidic (around pH 6.0–6.5)
- Infection progression is associated with increased alkalinity (above pH 7.2)

This project explores whether rule-based analysis of pH time-series data can simulate early infection detection.

---

## System Pipeline

Raw pH Data
    ↓
Rule-based Classification Model
    ↓
Labeled Dataset (Healthy / Risk / Infected)
    ↓
Visualization Engine
    ↓
Final Outputs (Graph + Summary Report)

---

## Methodology

The system applies threshold-based classification rules:

| pH Range | Condition |
|----------|----------|
| ≤ 6.5 | Healthy |
| 6.5 – 7.2 | Risk |
| > 7.2 | Infected |

Each measurement is evaluated independently to simulate continuous wound monitoring over time.

---

## Outputs

### Labeled Dataset
outputs/labeled_ph_data.csv

### Visualization
outputs/wound_ph_plot.png

### Summary Report
outputs/summary.txt

Example:
Infection detected at 36 hours.
pH crossed 7.2 threshold at 32 hours.

---

## Project Structure

data/
  pH.csv

code/
  model.py
  plot.py
  main.py

docs/
  methodology.md
  results.md
  limitations.md

outputs/
  labeled_ph_data.csv
  wound_ph_plot.png
  summary.txt

---

## Key Features

- Biomedical-inspired simulation of wound infection progression
- Time-series analysis of physiological data
- Transparent rule-based classification system
- Reproducible computational pipeline
- Structured scientific outputs

---

## Limitations

- Uses simulated data instead of clinical datasets
- Rule-based model without machine learning
- Not intended for medical diagnosis or clinical use
- Limited to pH as a single biological marker

---

## Future Work

- Multi-patient simulation environment
- Machine learning-based infection prediction
- Multi-sensor integration (temperature, oxygen, etc.)
- Real-time monitoring dashboard

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## Scientific Motivation

This project demonstrates how simple computational rules applied to biochemical signals can produce interpretable clinical states. It serves as a foundational simulation of biomedical monitoring systems for educational and research purposes.

---

## Author

Rabeh Mohamed Mehdi
