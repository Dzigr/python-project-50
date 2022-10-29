"""Input point."""
import argparse


FORMATTERS = ('stylish',)

def parse():
    """Parse data from user.

    Returns:
         parser.parse_args()
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=FORMATTERS,
        default="stylish",
        help='output format (default: %(default)s) ',
    )
    return parser.parse_args()
