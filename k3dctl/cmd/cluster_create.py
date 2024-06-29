import subprocess
import logging

from k3dctl.k3d import K3D
logger = logging.getLogger(__name__)

class ClusterCreateCommand:
    def __init__(self):
        self.k3dImpl = K3D()

    def execute(self, name):
        if(self.k3dImpl.cluster_exists(name)):
            logger.info(f"Cluster {name} exists. Skipping creation")
            return
        self.k3dImpl.create_cluster()
    