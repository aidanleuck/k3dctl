from argparse import ArgumentParser, Namespace
import subprocess
import logging
import os

from k3dctl.cmd.command import CLICommand
from k3dctl.k3d import K3D

logger = logging.getLogger(__name__)

class ClusterCreateCommand(CLICommand):
    def __init__(self):
        self.k3dImpl = K3D()

    def setup_args(self, parser: ArgumentParser):
        parser.add_argument("-c", "--configPath", action="store", default=os.environ.get("K3D_CONFIG_PATH"))

    def parse_args(self, args: Namespace) -> Namespace:
        if(not args.configPath):
            self.parser.print_help()
        
        return args

    def execute(self, args: Namespace) -> int:
        if(self.k3dImpl.cluster_exists("f")):
            logger.info(f"Cluster {args.name} exists. Skipping creation")
            return
        self.k3dImpl.create_cluster(args.configPath)

        return 0 # Success
    