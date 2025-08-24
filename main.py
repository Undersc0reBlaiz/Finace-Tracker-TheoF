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


# Example usage
load_transactions()
read_transaction_list()
add_transaction(25, "Food", "Lunch")
add_transaction(100, "Salary", "Weekly pay")
save_transactions()
add_transaction(60, "Lifestyle", "Salon")
read_transaction_list()
clear_history()