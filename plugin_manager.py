import importlib.util
import os
import sys
from typing import Dict, Any

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.plugin_dir = 'plugins'

    def load_plugins(self):
        if not os.path.exists(self.plugin_dir):
            os.makedirs(self.plugin_dir)

        for plugin_name in os.listdir(self.plugin_dir):
            plugin_path = os.path.join(self.plugin_dir, plugin_name)
            if os.path.isdir(plugin_path):
                self._load_plugin(plugin_name, plugin_path)

    def _load_plugin(self, plugin_name: str, plugin_path: str):
        init_file = os.path.join(plugin_path, '__init__.py')
        if os.path.exists(init_file):
            spec = importlib.util.spec_from_file_location(
                plugin_name, init_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[plugin_name] = module
            spec.loader.exec_module(module)
            self.plugins[plugin_name] = module

    def get_plugin(self, name: str) -> Any:
        return self.plugins.get(name)

    def execute_plugin(self, name: str, *args):
        plugin = self.get_plugin(name)
        if plugin:
            return plugin.main(*args)
        raise ValueError(f"Plugin {name} not found")