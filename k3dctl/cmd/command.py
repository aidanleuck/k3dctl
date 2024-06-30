from argparse import ArgumentParser, Namespace


class CLICommand():
    def __init__(self):
        self.name = ""
        self.parser = None
        pass
    def execute(self) -> int:
        raise "NO"
    def parse_args(self, args: Namespace) -> Namespace:
        return args
    def setup_parser(self, parser: ArgumentParser):
        pass
        