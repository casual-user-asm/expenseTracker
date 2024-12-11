# ExpenseTracker

Simple expense tracker application to manage your finances. The application allow users to add, delete, and view their expenses.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```python
python expense.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ python expense.py add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ python expense.py list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ python expense.py summary
# Total expenses: $30

$ python expense.py delete --id 2
# Expense deleted successfully

$ python expense.py summary
# Total expenses: $20

$ python expense.py summary --month 8
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
