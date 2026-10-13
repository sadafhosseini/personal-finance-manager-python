from database import add_transaction, get_transactions
from datetime import datetime



def add_income(title, amount, category):
    """
    Add income transaction
    """

    add_transaction(
        title,
        amount,
        category,
        "income",
        get_date()
    )

    print("Income added successfully.")



def add_expense(title, amount, category):
    """
    Add expense transaction
    """

    add_transaction(
        title,
        amount,
        category,
        "expense",
        get_date()
    )

    print("Expense added successfully.")



def get_date():

    return datetime.now().strftime(
        "%Y-%m-%d"
    )



def calculate_balance():

    transactions = get_transactions()

    income = 0
    expense = 0


    for item in transactions:

        amount = item[2]
        transaction_type = item[4]


        if transaction_type == "income":

            income += amount

        else:

            expense += amount


    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }



def get_category_summary():

    transactions = get_transactions()

    summary = {}


    for item in transactions:

        category = item[3]
        amount = item[2]
        transaction_type = item[4]


        if transaction_type == "expense":

            if category not in summary:
                summary[category] = 0

            summary[category] += amount


    return summary
