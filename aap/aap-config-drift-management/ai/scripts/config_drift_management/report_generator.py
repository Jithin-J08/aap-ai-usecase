class ReportGenerator:
    """Class to generate reports based on detected anomalies and configuration drift analysis."""
    
    def __init__(self):
        pass

    def generate_anomaly_report(self, anomalies):
        """Generate a report for detected anomalies."""
        if not anomalies:
            return "No anomalies detected."
        
        report = "Detected Anomalies:\n"
        for key, values in anomalies.items():
            report += f"{key}: Expected '{values['expected']}', but found '{values['current']}'\n"
        
        return report

    def generate_drift_report(self, drift_info):
        """Generate a report for configuration drift analysis."""
        if not drift_info:
            return "No configuration drift detected."
        
        report = "Configuration Drift Report:\n"
        for key, value in drift_info.items():
            report += f"{key}: Drift detected with value '{value}'\n"
        
        return report

    def save_report_to_file(self, report, filename):
        """Save the generated report to a specified file."""
        with open(filename, 'w') as file:
            file.write(report)