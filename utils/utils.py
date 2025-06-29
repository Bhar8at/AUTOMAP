import argparse

def get_args():
    parser = argparse.ArgumentParser(description="AUTOMAP Training Script")
    parser.add_argument(
        '-c', '--config',
        dest='config',
        required=True,
        help='Path to the configuration file')
    return parser.parse_args()
