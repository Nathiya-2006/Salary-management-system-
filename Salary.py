import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class FinanceAssistant:
    def __init__(self):
        self.data = pd.DataFrame(columns=["Date", "Type", "Category", "Amount"])

    def add_transaction(self, date, t_type, category, amount):
        try:
            date = pd.to_datetime(date, format="%Y-%m-%d")
            if t_type not in ["Income", "Expense"]:
                print("Error: Type must be 'Income' or 'Expense'.")
                return
            self.data.loc[len(self.data)] = [date, t_type, category, amount]
            print("Transaction added successfully.")
        except Exception as e:
            print("Error in transaction:", e)

    def show_summary(self):
        income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        expense = self.data[self.data["Type"] == "Expense"]["Amount"].sum()
        print(f"Income: ${income:.2f} | Expense: ${expense:.2f} | Savings: ${income - expense:.2f}")

    def categorize_expenses(self):
        expenses = self.data[self.data["Type"] == "Expense"]
        if expenses.empty:
            print("No expense data.")
        else:
            print("\nExpenses by Category:")
            print(expenses.groupby("Category")["Amount"].sum())

    def give_advice(self):
        income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        expense = self.data[self.data["Type"] == "Expense"]["Amount"].sum()
        if income == 0:
            print("No income data entered.")
            return
        rate = (income - expense) / income
        if expense > income:
            print("Overspending. Cut costs.")
        elif rate < 0.2:
            print("Save more. Target at least 20% of income.")
        else:
            print("Good job! You're saving well.")

    def predict_expense(self):
        expenses = self.data[self.data["Type"] == "Expense"]
        if expenses.empty:
            print("No expense data to predict.")
        else:
            avg = expenses["Amount"].mean()
            print(f"Predicted next month expense: ${avg:.2f}")

    def visualize(self):
        if self.data.empty:
            print("No data to visualize.")
            return
        df = self.data.copy()
        df["Month"] = df["Date"].dt.to_period("M")
        summary = df.groupby(["Month", "Type"])["Amount"].sum().unstack().fillna(0)
        summary.plot(kind="bar", stacked=True)
        plt.title("Monthly Income vs Expenses")
        plt.ylabel("Amount ($)")
        plt.xlabel("Month")
        plt.tight_layout()
        plt.show()

def main():
    fa = FinanceAssistant()
    while True:
        print("\n1. Add Transaction")
        print("2. Show Summary")
        print("3. Categorize Expenses")
        print("4. Financial Advice")
        print("5. Predict Next Month's Expense")
        print("6. Visualize")
        print("7. Exit")
        choice = input("Choose (1–7): ")

        if choice == "1":
            d = input("Date (YYYY-MM-DD): ")
            t = input("Type (Income/Expense): ").capitalize()
            c = input("Category: ")
            try:
                a = float(input("Amount: "))
                fa.add_transaction(d, t, c, a)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            fa.show_summary()
        elif choice == "3":
            fa.categorize_expenses()
        elif choice == "4":
            fa.give_advice()
        elif choice == "5":
            fa.predict_expense()
        elif choice == "6":
            fa.visualize()
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select between 1–7.")

if __name__ == "__main__":
    main()
