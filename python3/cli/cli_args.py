#!/usr/bin/env python3

from argparse import ArgumentParser
import sys  # 

def read_args():
    """Parse command-line arguments for name and optional age."""
    parser = ArgumentParser(description='Process command-line arguments')
    parser.add_argument('name', help='Your name')
    parser.add_argument('--age', type=int, help='Your age (optional)')
    args = parser.parse_args()
    return args

def main():
    """Process command-line arguments and print name and age if valid."""
    print(f'Script name: {sys.argv[0]}')
    print(f'Arguments: {sys.argv[1:]}')

    if len(sys.argv[1:]) > 0:
        try:
            args = read_args()
            if not args.name.strip():
                print("Error: Name cannot be empty", file=sys.stderr)
                return 1
            if args.name:
                print(f'Name: {args.name}')
            if args.age is not None:
                if args.age < 0:
                    print("Error: Age cannot be negative", file=sys.stderr)
                    return 1
                print(f'Age: {args.age}')
            return 0
        except SystemExit as e:
            return e.code
    return 0

if __name__ == '__main__':
    exit(main())
