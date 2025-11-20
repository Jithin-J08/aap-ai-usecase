class DriftDetector:
    """Class to analyze configuration drift."""

    def __init__(self, current_config, expected_config):
        self.current_config = current_config
        self.expected_config = expected_config

    def analyze_drift(self):
        """Analyze the drift between current and expected configurations."""
        drift = {}
        for key, expected_value in self.expected_config.items():
            current_value = self.current_config.get(key)
            if current_value != expected_value:
                drift[key] = {
                    'expected': expected_value,
                    'current': current_value
                }
        return drift

    def is_drift_detected(self):
        """Check if any drift is detected."""
        return bool(self.analyze_drift())