import csv
from datetime import datetime
import schedule
import time
import calendar

# Create an expense file
FILE_NAME = "expenses.csv"


# Function to add a new_expense
def add_expense(date, category, description, amount):
    with open(FILE_NAME, mode="a", newline="") as file:
        # A writer object. I think of it as creating a person with
        # Common sense able to handle punctuation and stuff.
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])


# Read the expenses
def read_expenses():
    # An empty array for the expenses to be added and read.
    expenses = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)
    return expenses


# Generate a monthly report
def generate_report():
    # Variable for today
    today = datetime.today()
    # Variable for the last day of the month.
    last_day = calendar.monthrange(today.year, today.month)[1]
    expenses = read_expenses()
    # Group by category and months.
    category_totals = {}
    monthly_totals = {}

    # Define the spending limitd for the diferrent categories.
    spending_limits = {
        "Food": 2000,
        "Transport": 1200,
        "Entertainment": 1000,
        "Other": 800
    }

    for row in expenses:
        # Format of a row
        date, category, description, amount = row
        # convert amount into float
        amount = float(amount)
        # Format the month.
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")

        # Category totals
        category_totals[category] = category_totals.get(category, 0) + amount

        # Monthly totals
        monthly_totals[month] = monthly_totals.get(month, 0) + amount
    if today.day == last_day or True:
        print("=== Monthly Report ===")
        print("Category Totals: ", category_totals)
        print("Monthly Totals: ", monthly_totals)

    print("\n===For Overspending Alerts!!===")
    for category, total in category_totals.items():
        if category in spending_limits and total > spending_limits[category]:
            print(f"Overspending in {category}!: {total} (Limit: {spending_limits[category]})")


# Automate report monthly
schedule.every().day.at("00:00").do(generate_report)

while True:
    schedule.run_pending()
    time.sleep(1)

generate_report()
