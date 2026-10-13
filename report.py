from finance import calculate_balance, get_category_summary



def show_financial_report():

    print("\n" + "=" * 35)
    print("       FINANCIAL REPORT")
    print("=" * 35)


    data = calculate_balance()


    print(f"""
Total Income: ${data['income']}
Total Expense: ${data['expense']}
Current Balance: ${data['balance']}
""")


def show_category_report():

    print("\n" + "=" * 35)
    print("      EXPENSE CATEGORIES")
    print("=" * 35)


    categories = get_category_summary()


    if not categories:

        print("No expense data available.")
        return


    total = sum(categories.values())


    for category, amount in categories.items():

        percentage = (
            amount / total * 100
        )

        print(
            f"{category}: "
            f"${amount} "
            f"({percentage:.2f}%)"
        )



def generate_summary():

    balance = calculate_balance()

    categories = get_category_summary()


    return {

        "balance": balance["balance"],

        "top_category":
            max(
                categories,
                key=categories.get
            )
            if categories
            else None

    }
