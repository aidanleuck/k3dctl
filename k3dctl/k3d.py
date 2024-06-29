import subprocess
import json

K3D_EXECUTABLE = "k3d"

class K3D: 
    def create_cluster(self, name: str, configPath: str) -> None:
        result = subprocess.run([K3D_EXECUTABLE, "cluster", "create", name, "--config", configPath])
        result.check_returncode()
    
    def get_clusters(self):
        result = subprocess.run([K3D_EXECUTABLE, "cluster", "list", "-o", "json"], stdout=subprocess.PIPE)
        result.check_returncode()

        stdout_string = result.stdout.decode()
        array = json.loads(stdout_string)

        return array

    def check_cluster_list(self, name: str, clusterList: list) -> bool:
        for item in clusterList:
            if item.name == name:
                return True
        
        return False
    
    def cluster_exists(self, name:str) -> bool:
        clusters = self.get_clusters()
        return self.check_cluster_list(name, clusters)
    


        