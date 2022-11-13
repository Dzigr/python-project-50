"""Main module."""
# !/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.generate_diff import generate_diff


def main():
    """Request fot two files."""
    try:
        args = parse_arguments()
    except BaseException:  # noqa: WPS424
        print('Check if the utility is being used correctly.')
    else:
        print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
