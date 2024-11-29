import argparse
import json
from rich import print


def load_expenses():
	try:
		with open ("tasks.json", 'r') as file:
			return json.load(file)
	except:
		print('File not found')
		return {}


def save_expenses(task):
	with open ('tasks.json', 'w') as file:
		json.dump(task, file, indent=4)

expenses = load_expenses()

parser = argparse.ArgumentParser(prog='tracker', description="Your expense tracker")
subparsers = parser.add_subparsers()

# 'add' subcommand
parser_add = subparsers.add_parser('add', help='Add expense to your list')
parser_add.add_argument('--description', type=str, required=True, help="Expense description")
parser_add.add_argument('--amount', type=int, required=True, help="Expense amount")

# 'update' subcommand
parser_update = subparsers.add_parser('update', help='Update an existing expense')
parser_update.add_argument('--id', type=str, required=True, help="Expense ID to update")
parser_update.add_argument('--update', type=str, help="New expense description")
parser_update.add_argument('--amount', type=int, help="New expense amount")


# 'delete' subcommand
parser_delete = subparsers.add_parser('delete', help='Remove existing expense')
parser_delete.add_argument('--id', required=True, help="Expense ID to delete")

args = parser.parse_args()

if hasattr(args, 'update'):
    if args.id in expenses:
        expenses[args.id] = {'description': args.update, 'amount': f"{args.amount}$"}
        save_expenses(expenses)
    else:
        print(f"Error: Expense with ID {args.id} not found.")
        
# 'add' logic
elif hasattr(args, 'description'):
    # Assign the next available ID
    expenses[len(expenses) + 1] = {'description': args.description, 'amount': f"{args.amount}$"}
    save_expenses(expenses)

# 'delete' logic
else:
    if args.id in expenses:
        del expenses[args.id]
        save_expenses(expenses)
    else:
        print(f"Error: Expense with ID {args.id} not found.")

print(expenses)