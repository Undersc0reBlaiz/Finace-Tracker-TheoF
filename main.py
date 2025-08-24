 # main.py
import datetime

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


# Example usage
add_transaction(25, "Food", "Lunch")
add_transaction(100, "Salary", "Weekly pay")

read_transaction_list()