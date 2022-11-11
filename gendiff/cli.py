"""Input point."""
import argparse

FORMATTERS = (
    'stylish',
    'plain',
    'json',
)


def parse():
    """Parse data from user.

    Returns:
         parser.parse_args()
    """
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=FORMATTERS,
        default='stylish',
        help='output format (default: %(default)s) ',  # noqa: WPS323
    )
    return parser.parse_args()
