# Configuration Drift Management

This project is designed to manage and detect configuration drift in systems. It provides tools to compare current system configurations against expected configurations, identify anomalies, and generate reports for further analysis.

## Project Structure

- **ai/scripts/anomaly_detection.py**: Contains functions to load current and expected configurations, detect anomalies, generate reports, and execute the anomaly detection process.
  
- **ai/scripts/config_drift_management/**: A package that includes:
  - **__init__.py**: Marks the directory as a Python package.
  - **drift_detector.py**: Defines the `DriftDetector` class for analyzing configuration drift.
  - **config_loader.py**: Defines the `ConfigLoader` class for loading configurations from various sources.
  - **report_generator.py**: Defines the `ReportGenerator` class for creating and formatting reports based on detected anomalies.

## Usage

1. Ensure that the expected configuration file (`expected_configuration.json`) is present in the project directory.
2. Run the `anomaly_detection.py` script to load the current configuration, compare it with the expected configuration, and generate a report of any detected anomalies.

## Requirements

- Python 3.x
- Required libraries: `json`, `subprocess`, `logging`

## License

This project is licensed under the MIT License. See the LICENSE file for more details.