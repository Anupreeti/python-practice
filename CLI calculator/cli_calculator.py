import argparse

parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument("num1", type=float,help="First Number")
parser.add_argument("num2",type=float,help="Second Number")
parser.add_argument("operation", choices=["add","sub","mul","div"], help="Operation")

args = parser.parse_args()

if args.operation == 'add':
    result = args.num1 + args.num2
elif args.operation == 'sub':
    result = args.num1 - args.num2
elif args.operation == 'mul':
    result = args.num1 * args.num2
elif args.operation == 'div':
    result = args.num1/args.num2

print(f"Result = {result}")
