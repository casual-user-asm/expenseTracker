import argparse
import json
from rich.console import Console
from datetime import datetime
from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", width=12)
table.add_column("ID")
table.add_column("Description", justify="center")
table.add_column("Amount", justify="center")
current_time = datetime.now()
create_time = current_time.strftime("%d.%m.%Y")


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except:
        print("File not found")
        return {}


def save_expenses(task):
    with open("expenses.json", "w") as file:
        json.dump(task, file, indent=4)


expenses = load_expenses()


def add_expenses(description, amount):
    next_id = max([int(key) for key in expenses.keys()], default=0) + 1
    expenses[next_id] = {
        "date": create_time,
        "description": description,
        "amount": f"{amount}$",
    }
    save_expenses(expenses)
    console.print(f"Expnese added with ID {next_id}", style="bold green")


def update_expenses(id, description, amount):
    if id in expenses:
        expenses[id] = {
            "date": create_time,
            "description": description,
            "amount": f"{amount}$",
        }
        save_expenses(expenses)
        console.print("Expense updated", style="bold blue")
    else:
        console.print(f"Error: Expense with ID {id} not found.", style="bold red")


def delete_expenses(id):
    if id in expenses:
        del expenses[id]
        save_expenses(expenses)
        console.print("Expense deleted", style="bold red")
    else:
        console.print(f"Error: Expense with ID {id} not found.", style="bold red")


def list_expenses():
    for k, v in expenses.items():
        table.add_row(v.get("date"), k, v.get("description"), v.get("amount"))
    console.print(table)


def summary_expenses(month=None):
    res = 0
    if month:
        for k, v in expenses.items():
            split_date = v.get("date").split(".")
            if month == split_date[1]:
                res += int(v["amount"].replace("$", ""))
    else:
        for k, v in expenses.items():
            res += int(v["amount"].replace("$", ""))
    console.print(f"Total expenses {res}$", style="bold yellow")


parser = argparse.ArgumentParser(prog="tracker", description="Your expense tracker")
subparsers = parser.add_subparsers(dest="command")

# 'add' subcommand
parser_add = subparsers.add_parser("add", help="Add expense to your list")
parser_add.add_argument(
    "--description", type=str, required=True, help="Expense description"
)
parser_add.add_argument("--amount", type=int, required=True, help="Expense amount")

# 'update' subcommand
parser_update = subparsers.add_parser("update", help="Update an existing expense")
parser_update.add_argument("--id", type=str, required=True, help="Expense ID to update")
parser_update.add_argument("--description", type=str, help="New expense description")
parser_update.add_argument("--amount", type=int, help="New expense amount")


# 'delete' subcommand
parser_delete = subparsers.add_parser("delete", help="Remove existing expense")
parser_delete.add_argument("--id", required=True, help="Expense ID to delete")

parser_summary = subparsers.add_parser(
    "summary", help="View summary of all your expenses"
)
parser_summary.add_argument("--month", help="View expenses for certain month")

parser_list = subparsers.add_parser("list", help="View info about all your expenses")

args = parser.parse_args()


match args.command:
    case "add":
        add_expenses(args.description, args.amount)
    case "update":
        update_expenses(args.id, args.description, args.amount)
    case "delete":
        delete_expenses(args.id)
    case "list":
        list_expenses()
    case "summary":
        summary_expenses(args.month)
