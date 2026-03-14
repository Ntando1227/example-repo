
# Combined Portfolio: Personal Finance + Loan/Credit Risk Scoring
# Interactive dashboard with tables, goals, alerts, and risk analysis

import matplotlib.pyplot as plt
from tabulate import tabulate



# Personal Finance Functions


def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: R"))
            if income < 0:
                print("Income cannot be negative. Try again.")
            else:
                return income
        except ValueError:
            print("Please enter a valid number.")


def get_expenses():
    expenses = {}
    print("\nEnter your monthly expenses for the following categories:")
    categories = ["Rent / Mortgage", "Utilities", "Groceries", "Transport", "Entertainment", "Others"]

    for category in categories:
        while True:
            try:
                amount = float(input(f"{category}: R"))
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    expenses[category] = amount
                    break
            except ValueError:
                print("Please enter a valid number.")
    return expenses


def get_savings_goal():
    while True:
        try:
            goal = float(input("\nEnter your savings goal for this month (R): "))
            if goal < 0:
                print("Goal cannot be negative. Try again.")
            else:
                return goal
        except ValueError:
            print("Please enter a valid number.")


def calculate_summary(income, expenses):
    total_expenses = sum(expenses.values())
    balance = income - total_expenses
    return total_expenses, balance


def check_alerts(balance, savings_goal):
    if balance < 0:
        print("\n⚠️ ALERT: You are overspending this month! Your expenses exceed your income.")
    elif balance < savings_goal:
        print(
            f"\n⚠️ ALERT: You did not meet your savings goal. You need R{savings_goal - balance:.2f} more to reach it.")
    else:
        print(f"\n✅ Great! You met your savings goal. Remaining balance: R{balance - savings_goal:.2f}")


def plot_expenses(expenses, month_name):
    labels = list(expenses.keys())
    amounts = list(expenses.values())
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"Expense Breakdown - {month_name}")
    plt.show()


def display_finance_table(months, incomes, total_expenses_list, balances, savings_goals):
    headers = ["Month", "Income", "Total Expenses", "Remaining Balance", "Savings Goal"]
    table = []
    for i, month in enumerate(months):
        table.append([
            month,
            f"R{incomes[i]:.2f}",
            f"R{total_expenses_list[i]:.2f}",
            f"R{balances[i]:.2f}",
            f"R{savings_goals[i]:.2f}"
        ])
    print("\n===== Personal Finance Summary Table =====")
    print(tabulate(table, headers=headers, tablefmt="grid"))


def plot_finance_trends(months, incomes, total_expenses_list, balances):
    plt.figure(figsize=(10, 5))
    plt.plot(months, incomes, marker='o', label="Income")
    plt.plot(months, total_expenses_list, marker='o', label="Total Expenses")
    plt.plot(months, balances, marker='o', label="Remaining Balance")
    plt.title("Financial Trends Over Months")
    plt.xlabel("Month")
    plt.ylabel("Amount (R)")
    plt.legend()
    plt.grid(True)
    plt.show()



# Loan / Credit Risk Functions


def get_applicant_info():
    print("\nEnter applicant details:")
    name = input("Name: ").strip()
    while True:
        try:
            age = int(input("Age: "))
            if age < 18:
                print("Applicant must be at least 18 years old.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            income = float(input("Monthly Income (R): "))
            if income < 0:
                print("Income cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            debt = float(input("Monthly Debt Payments (R): "))
            if debt < 0:
                print("Debt cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            credit_score = int(input("Credit Score (300-850): "))
            if 300 <= credit_score <= 850:
                break
            else:
                print("Credit score must be between 300 and 850.")
        except ValueError:
            print("Please enter a valid number.")

    return {
        "name": name,
        "age": age,
        "income": income,
        "debt": debt,
        "credit_score": credit_score
    }


def calculate_risk(applicant):
    income = applicant["income"]
    debt = applicant["debt"]
    credit_score = applicant["credit_score"]
    dti = debt / income
    if dti < 0.3 and credit_score >= 700:
        risk = "Low"
    elif dti < 0.4 and credit_score >= 650:
        risk = "Medium"
    else:
        risk = "High"
    return risk, dti


def display_applicant_summary(applicant, risk, dti):
    print("\n===== Applicant Risk Summary =====")
    print(f"Name: {applicant['name']}")
    print(f"Age: {applicant['age']}")
    print(f"Income: R{applicant['income']:.2f}")
    print(f"Debt: R{applicant['debt']:.2f}")
    print(f"Debt-to-Income Ratio: {dti:.2f}")
    print(f"Credit Score: {applicant['credit_score']}")
    print(f"Risk Level: {risk}")
    if risk == "High":
        print("⚠️ ALERT: High risk. Loan not recommended.")
    elif risk == "Medium":
        print("⚠️ ALERT: Moderate risk. Further evaluation needed.")
    else:
        print("✅ Low risk. Loan likely to be approved.")


def display_all_applicants_table(applicants):
    headers = ["Name", "Age", "Income", "Debt", "DTI", "Credit Score", "Risk Level"]
    table = []
    for a in applicants:
        table.append([
            a['name'],
            a['age'],
            f"R{a['income']:.2f}",
            f"R{a['debt']:.2f}",
            f"{a['dti']:.2f}",
            a['credit_score'],
            a['risk']
        ])
    print("\n===== All Applicants Summary Table =====")
    print(tabulate(table, headers=headers, tablefmt="grid"))


def plot_risk_distribution(applicants):
    risk_counts = {"Low": 0, "Medium": 0, "High": 0}
    for a in applicants:
        risk_counts[a["risk"]] += 1
    categories = list(risk_counts.keys())
    counts = list(risk_counts.values())
    plt.figure(figsize=(7, 5))
    plt.bar(categories, counts, color=["green", "orange", "red"])
    plt.title("Loan Applicant Risk Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Applicants")
    plt.show()


# Main Portfolio Dashboard

def main():
    print("Welcome to the Finance Portfolio Dashboard!\n")

    #Personal Finance Section
    months = []
    incomes = []
    total_expenses_list = []
    balances = []
    savings_goals = []

    num_months = int(input("How many months of personal finance would you like to track? "))
    for i in range(1, num_months + 1):
        print(f"\n--- Month {i} ---")
        months.append(f"Month {i}")
        income = get_income()
        expenses = get_expenses()
        savings_goal = get_savings_goal()

        total_expenses, balance = calculate_summary(income, expenses)

        incomes.append(income)
        total_expenses_list.append(total_expenses)
        balances.append(balance)
        savings_goals.append(savings_goal)

        print(f"\nMonth {i} Summary:")
        print(f"Income: R{income:.2f}, Total Expenses: R{total_expenses:.2f}, Remaining Balance: R{balance:.2f}")
        check_alerts(balance, savings_goal)
        plot_expenses(expenses, months[-1])

    display_finance_table(months, incomes, total_expenses_list, balances, savings_goals)
    plot_finance_trends(months, incomes, total_expenses_list, balances)

    #Loan Risk Section
    applicants = []
    print("\n\n--- Loan / Credit Risk Scoring Section ---")
    while True:
        applicant = get_applicant_info()
        risk, dti = calculate_risk(applicant)
        display_applicant_summary(applicant, risk, dti)
        applicants.append({**applicant, "risk": risk, "dti": dti})

        cont = input("\nEnter another applicant? (y/n): ").lower()
        if cont != "y":
            break

    display_all_applicants_table(applicants)
    plot_risk_distribution(applicants)

    print("\nThank you for using the Finance Portfolio Dashboard!")


if __name__ == "__main__":
    main()
