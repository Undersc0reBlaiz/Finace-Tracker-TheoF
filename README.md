# Personal Finance Tracker (Early Version)

A simple Python program to record and display financial transactions.  
This is an early stage of a personal project to build a more complete **Personal Finance Tracker**.
The project is currently coded completely in Python and requires Python 3.8 or later to run. No external libraries at this stage.


## Features (Current Stage)

- Add transactions with:
  - Date (auto-generated as today’s date)
  - Amount
  - Category (e.g., Food, Salary, Transport)
  - Description
- Display all recorded transactions in a table format.

## Project Structure
personal-finance-tracker/
─ main.py # Core program
─ README.md # Documentation (this file)

## Example Output
When you run the code currently this is the output:
Date         | Amount  |  Category  | Description
---------------------------------------------
2025-08-24   |    25   |    Food    |       Lunch
2025-08-24   |   100   |   Salary   |   Weekly pay

## Next Steps
- Saving Transactions to csv file
- Load past transactions on program start
- Add summaries (totals, per month, categories...)
- Improve input options
- Add charts via Matplotlib
