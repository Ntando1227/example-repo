# loan_risk_scoring_portfolio.py
# Loan / Credit Risk Scoring System with Table and Risk Distribution Graph

import matplotlib.pyplot as plt
from tabulate import tabulate


# ----------------------------
# Input Functions
# ----------------------------

def get_applicant_info():
    """Get user input for loan applicant"""
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


# ----------------------------
# Risk Scoring Logic
# ----------------------------

def calculate_risk(applicant):
    """Assign a risk category based on simple rules"""
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


# ----------------------------
# Display Functions
# ----------------------------

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
    """Plot number of applicants in each risk category"""
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


# ----------------------------
# Main Program
# ----------------------------

def main():
    print("Welcome to the Loan / Credit Risk Scoring System!\n")

    applicants = []
    while True:
        applicant = get_applicant_info()
        risk, dti = calculate_risk(applicant)
        display_applicant_summary(applicant, risk, dti)

        # Save applicant
        applicants.append({
            **applicant,
            "risk": risk,
            "dti": dti
        })

        cont = input("\nEnter another applicant? (y/n): ").lower()
        if cont != "y":
            break

    # Display full table and plot
    display_all_applicants_table(applicants)
    plot_risk_distribution(applicants)

    print(f"\nTotal applicants processed: {len(applicants)}")
    print("Thank you for using the Loan Risk Scoring System!")


if __name__ == "__main__":
    main()
