
from k3dctl import __app_name__
from k3dctl.cmd.cluster_create import ClusterCreateCommand

def main():
    create_command = ClusterCreateCommand()
    create_command.execute("BOO", "")
    
if __name__ == "__main__":
    main()