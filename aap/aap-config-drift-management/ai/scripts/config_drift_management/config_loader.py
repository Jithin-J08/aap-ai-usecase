class ConfigLoader:
    """Class to load configurations from various sources."""
    
    def load_from_file(self, file_path):
        """Load configuration from a specified file."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error loading configuration from file {file_path}: {e}")
            return {}

    def load_from_env(self, env_var):
        """Load configuration from an environment variable."""
        value = os.getenv(env_var)
        if value is not None:
            return json.loads(value)
        else:
            logging.warning(f"Environment variable {env_var} not found.")
            return {}

    def load_from_multiple_sources(self, sources):
        """Load configuration from multiple sources."""
        config = {}
        for source in sources:
            if source['type'] == 'file':
                config.update(self.load_from_file(source['path']))
            elif source['type'] == 'env':
                config.update(self.load_from_env(source['var']))
        return config