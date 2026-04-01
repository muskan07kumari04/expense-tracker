import csv
import os
from datetime import date

# ──────────────────────────────────────────
#  The file where all expenses will be saved
# ──────────────────────────────────────────
FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it doesn't exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
        print("✅ New expense file created!\n")


def add_expense():
    """Ask the user for expense details and save it to the file."""
    print("\n─── Add New Expense ───")

    # Show category options
    print("Categories: 1) Food  2) Transport  3) Shopping  4) Bills  5) Other")
    category_map = {
        "1": "Food",
        "2": "Transport",
        "3": "Shopping",
        "4": "Bills",
        "5": "Other"
    }
    choice = input("Choose category (1-5): ").strip()
    category = category_map.get(choice, "Other")

    description = input("Description (e.g. Lunch, Bus fare): ").strip()

    # Make sure the amount is a valid number
    while True:
        try:
            amount = float(input("Amount spent (₹): ").strip())
            break
        except ValueError:
            print("⚠️  Please enter a valid number.")

    today = str(date.today())  # Automatically gets today's date

    # Save to CSV file
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, description, amount])

    print(f"✅ Expense of ₹{amount:.2f} added successfully!\n")


def view_expenses():
    """Read and display all saved expenses in a neat table."""
    print("\n─── All Expenses ───")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.\n")
        return

    # Print table header
    print(f"{'#':<4} {'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>10}")
    print("─" * 62)

    # Print each expense row (skip the header row)
    for i, row in enumerate(rows[1:], start=1):
        date_val, category, description, amount = row
        print(f"{i:<4} {date_val:<12} {category:<12} {description:<20} ₹{float(amount):>9.2f}")

    print()


def view_total():
    """Calculate and display the total amount spent."""
    print("\n─── Total Summary ───")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        rows = list(reader)

    if not rows:
        print("No expenses to calculate.\n")
        return

    # Add up all amounts
    total = sum(float(row[3]) for row in rows)
    count = len(rows)

    print(f"Total expenses recorded : {count}")
    print(f"Total amount spent      : ₹{total:.2f}\n")


def view_by_category():
    """Show total spending broken down by category."""
    print("\n─── Spending by Category ───")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    # Group totals by category
    category_totals = {}
    for row in rows:
        category = row[1]
        amount = float(row[3])
        category_totals[category] = category_totals.get(category, 0) + amount

    # Display results
    for category, total in sorted(category_totals.items()):
        print(f"  {category:<15} ₹{total:.2f}")
    print()


def main():
    """Main menu loop — keeps the program running until user exits."""
    initialize_file()

    print("=" * 40)
    print("   💰 Expense Tracker — by Muskan")
    print("=" * 40)

    while True:
        print("What would you like to do?")
        print("  1. Add an expense")
        print("  2. View all expenses")
        print("  3. View total spent")
        print("  4. View spending by category")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            print("\n👋 Goodbye! Keep tracking those expenses, Muskan!\n")
            break
        else:
            print("⚠️  Invalid choice. Please enter a number between 1 and 5.\n")


# ── Entry point ──
if __name__ == "__main__":
    main()