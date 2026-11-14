from datetime import date,datetime

# Add a new expense
def add_expense(expenses):

    print("Please add an expense:")
    while True:
        title = input("Title: ").strip()
        if not title:
            print("Title can not be Empty")
            continue
        break

    while True:
        try:
            amount = int(input("Amount: "))
            if amount<=0:
                print("Amount can't be negative or zero")
                continue

            break
        except ValueError :
            print("	Amount must be a number.")

    while True:
        category = input("Category: ").strip()
        if not category:
            print("Category can not be Empty")
            continue
        break

    today_data=date.today().isoformat()

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category,
        "date":today_data
    })
    print("Expense successfully added!")
    print()

# Display all expenses
def show_expenses(expenses):
    if not expenses:
        print("Your list is empty. Add an expense first!")
    else:
        print("===== EXPENSES =====")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['title']} | {expense['amount']} | {expense['category']} | {expense['date']}")

    print()

# Calculate total expenses
def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total}")
    print()

# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("Your list is empty. Add an expense first!")
    else:
        while True:
            try:
                delete_num = int(input("Please enter a number that you want to delete: "))
                if not 1 <= delete_num <= len(expenses):
                    print("Invalid expense number!")
                    continue
                deleted_expense = expenses.pop(delete_num - 1)
                print(f"'{deleted_expense['title']}' successfully deleted!")
                break

            except ValueError:
                print("You must enter a number")
    print()

# Filter expenses by category
def filter_by_category(expenses):
    if not expenses:
        print("Your list is empty. Add an expense first!")
        return
    while True:
        category=input("Please Enter a category: ").strip()
        if not  category:
            print("Category must not be Empty")
            continue
        filtered_expenses = [
            expense
            for expense in expenses
            if category.lower()== expense['category'].lower()
        ]
        if filtered_expenses:
            for index,expense in enumerate(filtered_expenses,start=1):
                print(f"{index}. {expense['title']} | {expense['amount']} | {expense['category']} | {expense['date']}")
            break
        else:
            print("The Category doesn't exist.")
            continue

    print()

# Generate a report of expenses by category
def show_category_report(expenses):
    if not expenses:
        print("Your list is empty. Add an expense first!")
        return
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        category_totals[category] = category_totals.get(category, 0) + amount

    print("===== CATEGORY REPORT =====")
    for key,value in category_totals.items():
        print(f"{key}: {value}")

# Generate a monthly expense report
def monthly_report(expenses):
    if not expenses:
        print("Your list is empty. Add an expense first!")
        return
    monthly_expenses={}
    for expense in expenses:
        # Group expenses by year and month
        date_key=datetime.strptime(expense['date'],"%Y-%m-%d")
        amount=expense['amount']
        month_key=date_key.strftime("%Y-%m")
        monthly_expenses[month_key] = monthly_expenses.get(month_key, 0) + amount

    print("===== MONTHLY REPORT =====")
    for key, value in monthly_expenses.items():
        print(f"{key}: {value}")
    print()

expenses=[]

# Main program loop
while True:
    print("""===== EXPENSE TRACKER =====
1. Add expense
2. Show expenses
3. Show total
4. Delete expense
5. Filter Category
6. Show Total Category
7. Monthly Report
8. Exit""")
    print()
    option = input("Choose a number : ")
    if option == "1":
        add_expense(expenses)
    elif option == "2":
        show_expenses(expenses)
    elif option=="3":
        show_total(expenses)
    elif option=="4":
        delete_expense(expenses)
    elif option=="5":
        filter_by_category(expenses)
    elif option=="6":
        show_category_report(expenses)
    elif option=="7":
        monthly_report(expenses)
    elif option=="8":
        print("Goodbye!...")
        break
    else:
        print("You must enter a number between 1-8")




