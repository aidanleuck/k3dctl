
from k3dctl import __app_name__, __command_group__
import argparse
import logging
import sys

from k3dctl.cmd.cluster_create import ClusterCreateCommand
from k3dctl.cmd.command import CLICommand

COMMANDS = {
    "create-cluster": ClusterCreateCommand()
}

logger = logging.getLogger(__name__)
def __setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                    prog=__app_name__,
                    description='Wrapper for K3D to accomplish common tasks for use in devcontainers',
                    epilog='Text at the bottom of help')
    return parser

def main():
    parser = __setup_parser()
    subparser = parser.add_subparsers(dest="command", required=True)
    for k,v in COMMANDS.items():
        p = subparser.add_parser(k)
        v.setup_args(p)
        v.name = k
        
    parsed_args = parser.parse_args()
    command_to_run = COMMANDS.get(parsed_args.command)
    command_to_run.parser = parser

    if(not command_to_run):
        raise ValueError(f"No known command named {parsed_args.command}")
    
    command_to_run.parse_args(parsed_args)
    command_to_run.execute(parsed_args)

if __name__ == "__main__":
    main()