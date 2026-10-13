from database import create_tables, get_transactions, delete_transaction
from finance import add_income, add_expense
from report import show_financial_report, show_category_report



def show_menu():

    print("\n" + "=" * 40)
    print("      PERSONAL FINANCE MANAGER")
    print("=" * 40)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Financial Report")
    print("5. Expense Categories")
    print("6. Delete Transaction")
    print("7. Exit")



def show_transactions():

    transactions = get_transactions()


    if not transactions:

        print("No transactions found.")
        return


    print("\n--- TRANSACTIONS ---")


    for item in transactions:

        print(
            f"""
ID: {item[0]}
Title: {item[1]}
Amount: ${item[2]}
Category: {item[3]}
Type: {item[4]}
Date: {item[5]}
---------------------
"""
        )



def delete_transaction_menu():

    show_transactions()


    try:

        transaction_id = int(
            input(
                "Enter transaction ID to delete: "
            )
        )


        delete_transaction(
            transaction_id
        )


        print(
            "Transaction deleted."
        )


    except ValueError:

        print(
            "Invalid ID."
        )



def main():

    create_tables()


    while True:

        show_menu()


        choice = input(
            "\nChoose option: "
        )


        if choice == "1":

            title = input(
                "Income title: "
            )

            amount = float(
                input(
                    "Amount: "
                )
            )

            category = input(
                "Category: "
            )


            add_income(
                title,
                amount,
                category
            )



        elif choice == "2":

            title = input(
                "Expense title: "
            )

            amount = float(
                input(
                    "Amount: "
                )
            )

            category = input(
                "Category: "
            )


            add_expense(
                title,
                amount,
                category
            )



        elif choice == "3":

            show_transactions()



        elif choice == "4":

            show_financial_report()



        elif choice == "5":

            show_category_report()



        elif choice == "6":

            delete_transaction_menu()



        elif choice == "7":

            print(
                "Goodbye!"
            )

            break



        else:

            print(
                "Invalid option."
            )



if __name__ == "__main__":

    main()
