# Personal Finance Tracker (Early Version)

A simple Python program to record and display financial transactions.  
This is an early stage of a personal project to build a more complete **Personal Finance Tracker**.
The project is currently coded completely in Python and requires Python 3.8 or later to run. No external libraries at this stage.
Last update: 25/08/25


## Features (Current Stage)

- Add transactions with:
  - Date (auto-generated as today’s date)
  - Amount
  - Category (e.g., Food, Salary, Transport)
  - Description
- Display all recorded transactions in a table format.
- Accesses csv file to:
  - Save Transactions to csv file
  - Load Transactions on command
  - Clear Transaction history on command

## Project Structure
personal-finance-tracker/
- main.py # Core program
- README.md # Documentation (this file)
- TransactionsList.csv # csv file of stored data

## Next Steps
- Load past transactions on program start
- Add summaries (totals, per month, categories...)
- Improve input options
- Add charts via Matplotlib
