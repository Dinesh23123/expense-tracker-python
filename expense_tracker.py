# create a Expense Tracker Using Functions and File Handling

def add_expense():
    date = input("Enter Date: ")
    category = input("Enter category:")
    amount = input("Enter amount: ")

    with open("expense.txt", "a") as f:
        f.write(date + "," + category + "," + amount + "\n")
        print("Data Stored successfully")

def view_expense():
    with open("expense.txt", "r") as f:
        print(f.readlines())

def search_expense():
    search = input("Enter category to search: ")
    found = False

    with open("expense.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[1] == search:
                print("Expense is: ", data)
                found = True
        if not found:
            print("Expense not found")

def total_expense():
    total = 0
    with open("expense.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            total += int(data[2])
    print("Total Expense is: ", total)

def delete_expense():
    delete_date = input("Enter date of expense to delete: ")
    delete_category = input("Enter category: ")

    found = False                                 

    with open("expense.txt", "r") as f:
        lines = f.readlines()

    with open("expense.txt", "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == delete_date and data[1] == delete_category:
                found = True
            else:
                f.write(line)
    if found:
        print("Expense deleted successfully")
    else:
        print("Expense not found")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Show Total Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        search_expense()

    elif choice == "4":
        total_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


