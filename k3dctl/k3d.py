import subprocess
import json
import os

K3D_EXECUTABLE = "k3d"
CONFIG_PATH_ENV = "K3D_CONFIG_PATH"

class K3D: 
    def create_cluster(self, configPath) -> None:
        result = subprocess.run([K3D_EXECUTABLE, "cluster", "create", "--config", configPath])
        result.check_returncode()
    
    def get_clusters(self):
        result = subprocess.run([K3D_EXECUTABLE, "cluster", "list", "-o", "json"], stdout=subprocess.PIPE)
        result.check_returncode()

        stdout_string = result.stdout.decode()
        array = json.loads(stdout_string)

        return array
    
    def __get_config_path(self):
        return os.getenv(CONFIG_PATH_ENV)

    def check_cluster_list(self, name: str, clusterList: list) -> bool:
        for item in clusterList:
            if item.name == name:
                return True
        
        return False
    
    def cluster_exists(self, name:str) -> bool:
        clusters = self.get_clusters()
        return self.check_cluster_list(name, clusters)
    


        