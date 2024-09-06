# Function to calculate SSS contribution based on gross income
def compute_sss(gross_income):
    if gross_income <= 20000:
        return 125.75
    elif gross_income <= 50000:
        return 2200.50
    elif gross_income <= 75000:
        return 4800.00
    else:
        return 5800.00

# Function to calculate PhilHealth contribution based on gross income
def compute_philhealth(gross_income):
    if gross_income <= 20000:
        return 100.00
    elif gross_income <= 50000:
        return 1200.00
    elif gross_income <= 75000:
        return 6800.00
    else:
        return 8800.00

# Function to calculate Pag-IBIG contribution (fixed)
def compute_pagibig():
    return 100.00

# Main program to input employee details and calculate deductions and income
def main():
    # Input employee details
    employee_name = input("Enter employee's name: ")
    department = input("Enter employee's department: ")

    # Input values for calculating gross income
    rate_per_hour = float(input("Enter rate per hour: "))
    hours_per_day = float(input("Enter number of working hours per day: "))
    days_per_week = float(input("Enter number of days per week: "))
    weeks_per_month = float(input("Enter number of weeks per month: "))

    # Calculate gross income
    gross_income = hours_per_day * days_per_week * weeks_per_month * rate_per_hour

    # Calculate contributions and total deductions
    sss_contribution = compute_sss(gross_income)
    philhealth_contribution = compute_philhealth(gross_income)
    pagibig_contribution = compute_pagibig()

    total_deduction = sss_contribution + philhealth_contribution + pagibig_contribution

    # Calculate net income
    net_income = gross_income - total_deduction

    # Display the results
    print("\n--- Employee Salary Details ---")
    print(f"Employee Name: {employee_name}")
    print(f"Department: {department}")
    print(f"Gross Income: {gross_income:.2f}")
    print(f"Total Deductions: {total_deduction:.2f}")
    print(f"Net Income: {net_income:.2f}")

# Run the program
if __name__ == "__main__":
    main()


