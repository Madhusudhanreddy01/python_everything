import sqlite3

# Connect to the database
conn = sqlite3.connect('expense_tracker.db')
c = conn.cursor()

# Create the expenses table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             date TEXT,
             category TEXT,
             description TEXT,
             amount REAL)''')

def add_expense(date, category, description, amount):
    # Insert a new expense into the database
    c.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
              (date, category, description, amount))
    conn.commit()
    print("Expense added successfully.")

def view_expenses():
    # Retrieve all expenses from the database
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("Expense ID | Date       | Category    | Description                | Amount")
        print("-------------------------------------------------------------------------")
        for expense in expenses:
            print(f"{expense[0]:<11}| {expense[1]:<10}| {expense[2]:<12}| {expense[3]:<27}| ${expense[4]:.2f}")

def generate_report(criteria):
    # Generate a report based on the specified criteria
    if criteria == "monthly":
        c.execute("SELECT strftime('%m-%Y', date) AS month, SUM(amount) FROM expenses GROUP BY month")
        report = c.fetchall()
        if len(report) == 0:
            print("No expenses found for any month.")
        else:
            print("Month     | Total Amount")
            print("-----------------------")
            for entry in report:
                print(f"{entry[0]:<10}| ${entry[1]:.2f}")
    elif criteria == "category":
        c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        report = c.fetchall()
        if len(report) == 0:
            print("No expenses found for any category.")
        else:
            print("Category    | Total Amount")
            print("-------------------------")
            for entry in report:
                print(f"{entry[0]:<12}| ${entry[1]:.2f}")
    else:
        print("Invalid report criteria. Please choose 'monthly' or 'category'.")

# Main program loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report (Monthly)")
    print("4. Generate Report (Category)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))
        add_expense(date, category, description, amount)

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        generate_report("monthly")

    elif choice == '4':
        generate_report("category")

    elif choice == '5':
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
