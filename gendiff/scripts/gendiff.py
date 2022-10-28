"""Main module."""
# !/usr/bin/env python3
from gendiff.cli import parse
from gendiff.diff import generate_diff


def main():
    """Request fot two files."""
    args = parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
