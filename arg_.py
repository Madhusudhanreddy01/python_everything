import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, help="This is the first argument")
parser.add_argument('name')
parser.add_argument('age')

# Parse and print the results
args = parser.parse_args()
# print(args.argument1)
print(f'Hello {args.name}')
print(f'{args.name} is {args.age} years old')