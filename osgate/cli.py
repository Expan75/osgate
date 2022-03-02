from argparse import ArgumentParser

__VERSION__ = "0.0.1"
versioning_message = f"""
    osgate v{__VERSION__} | simple gateway for use within industrial IoT.
"""

def parse_args():
    parser = ArgumentParser(description="Argument parser")
    parser.add_argument(
        "--config",
        "-c",
        dest="config",
        type=str,
        help="Absolute Configuration filepath",
    )
    parser.add_argument(
        "--debug", "-d", dest="debug", action="store_true", help="Activate debug log"
    )
    parser.add_argument("-v", "--version", action="version", version=versioning_message)
    return parser.parse_args()
