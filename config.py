import os
import json
from typing import Any, Dict

class ConfigManager:
    def __init__(self):
        self.config_file = "toolbox_config.json"
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            'general': {
                'language': 'zh_CN',
                'theme': 'dark',
                'auto_update': True
            },
            'network': {
                'proxy': '',
                'timeout': 10
            },
            'security': {
                'encryption_key': '',
                'password_strength': 'strong'
            }
        }

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, section: str, key: str, default=None) -> Any:
        return self.config.get(section, {}).get(key, default)

    def set(self, section: str, key: str, value: Any):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value
        self.save_config()