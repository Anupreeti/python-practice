import csv
import argparse
from datetime import datetime
import os

def save_file(task):
    file_exists = os.path.exists("expenses.csv")
    headers = ["date","category","amount"]
    try:
        with open("expenses.csv", "a", newline="") as f:
            data = csv.DictWriter(f, fieldnames=headers)
            if not file_exists or os.path.getsize("expenses.csv") == 0:
                data.writeheader()
            data.writerow(task)
    except Exception as e:
        return e

def add_task(task_date, category, amount):
    task = {"date": task_date.isoformat(), "category": category, "amount": amount}
    error = save_file(task)
    if not error:
        print("Task addedd!")
    else:
        print(error)

def view_expense():
    try:
        with open("expenses.csv", "r") as f:
            data = csv.DictReader(f)
            category_totals={}
            for row in data:
                if not row['category'] or not row['amount']:
                    continue  # Skip incomplete rows
                cat = row['category']
                amt = int(row['amount'])
                category_totals[cat] = category_totals.get(cat, 0) + amt
            for cat, amt in category_totals.items():
                print(f"Total expense of {cat} category : {amt}")
    except FileNotFoundError as e:
        print("Error : ", e)

def view_task():
    try:
        with open("expenses.csv","r") as f:
            data = csv.DictReader(f)
            for row in data:
                print(row)
    except FileNotFoundError as e:
        print("Error : ",e)
def high_spending():
    try:
        with open("expenses.csv", "r") as f:
            data = csv.DictReader(f)
            date_totals = {}
            for row in data:
                dates = row['date']
                amt = int(row['amount'])
                date_totals[dates] = date_totals.get(dates, 0) + amt
            max_amount = 0
            max_date = ""
            for dates, amt in date_totals.items():
                if max_amount < amt:
                    max_amount = amt
                    max_date = dates
            print(f"Highest spending is done on {max_date} with total of {max_amount}")
    except FileNotFoundError as e:
        print("Error : ",e)

task={}
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Calculate Expenses")

    parser.add_argument("--task", choices=["add", "view","expense", "spending"], help="Enter the task to perform")
    parser.add_argument("--date", type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(), help="Enter date")
    parser.add_argument("--category", help="Enter expense category")
    parser.add_argument("--amount", help="Enter the amount spend")

    args = parser.parse_args()

    if args.task == "add":
        if args.date and args.category and args.amount:
            add_task(args.date, args.category, args.amount)
        else:
            print("Enter date, category and amount to add the task")
    if args.task == "view":
        view_task()

    if args.task == "expense":
        view_expense()

    if args.task == "spending":
        high_spending()
