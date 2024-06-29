import os

K3D_CONFIG_ENV = "K3D_CONFIG_PATH"

class K3DContext():
    def get_context(self, configPath: str | None):
       configPath = self.get_config_path()
        
    def get_config_path(self, configPath: str | None):
        if(configPath):
            return configPath
        
 