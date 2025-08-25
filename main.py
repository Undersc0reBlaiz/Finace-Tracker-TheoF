 # main.py
import datetime
import csv

#Full transactions list
TransactionsList = []


def add_transaction(amount, category, description):
    today = datetime.date.today().isoformat()
    #Create temporary dictionary "transaction"
    transaction = {
        "date": today,
        "amount": amount,
        "category": category,
        "description": description
    }
    TransactionsList.append(transaction)

def read_transaction_list():
    width = 45
    print(f"{'Date':<13}|{'Amount':^9}|{'Category':^12}|{'Description':>12}")
    print("-" * width)
    for t in TransactionsList:
        print(f"{t['date']:<13}|{t['amount']:^9}|{t['category']:^12}|{t['description']:>12}")

def save_transactions():
    with open("TransactionsList.csv", mode="w", newline="") as file:
        cols = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=cols)
        writer.writeheader()
        writer.writerows(TransactionsList)

def load_transactions():
    try:
        with open("TransactionsList.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                TransactionsList.append(row)
    except FileNotFoundError:
        pass

def clear_history():
    global TransactionsList
    TransactionsList = []
    with open("TransactionsList.csv", mode="w", newline="") as file:
        cols = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=cols)
        writer.writeheader()

# Main()
def main():
    load_transactions()
    print("\nWelcome to your Personal Finance Tracker")
    while True:
        print("\nTo proceed, please select an option from below:")
        selection = input("""
        [1] Add Transaction
        [2] View Transactions
        [3] Clear Transaction History
        [4] Exit
        """)
        if selection == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Salary): ")
                description = input("Enter description: ")
                add_transaction(amount, category, description)
                save_transactions()
            except ValueError:
                print("Invalid amount, please enter a number")
        elif selection == "2":
            read_transaction_list()
        elif selection == "3":
            confirm = input("Are you certain you want to clear all history? (y/n): ")
            if confirm.lower() == "y":
                clear_history()
        elif selection == "4":
            print("Thank you for using this Personal Finance Tracker")
            break
        else:
            print("Invalid selection, please choose 1-4")
    

if __name__ == "__main__":
    main()