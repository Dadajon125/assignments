family_name = input("Enter family name: ")
income = int(input("Enter combined monthly income: "))


mortgage, insurance, car_payment, utilities = map(int, input("Enter fixed expenses (Mortgage, Insurance, Car, Utilities): ").split())


groceries, childcare, activities = map(int, input("Enter variable expenses (Groceries, Childcare, Activities): ").split())

current_fund = int(input("Enter current vacation fund balance: "))
vacation_cost = int(input("Enter vacation cost target: "))
months = int(input("Enter months until vacation date: "))


total_fixed = mortgage + insurance + car_payment + utilities
total_variable = groceries + childcare + activities
total_expenses = total_fixed + total_variable

monthly_savings = income - total_expenses
savings_rate = (monthly_savings / income) * 100 if income > 0 else 0
projected_fund = current_fund + (monthly_savings * months)
total_needed = vacation_cost - current_fund
monthly_needed = total_needed / months
monthly_gap = monthly_savings - monthly_needed
total_gap = projected_fund - vacation_cost

emergency_status = savings_rate < 10
needs_improvement = 10 <= savings_rate < 15
stable = 15 <= savings_rate < 25
strong = savings_rate >= 25
vacation_affordable = projected_fund >= vacation_cost


print(f"\n--- Vacation Budget Report for {family_name} ---")
print(f"Monthly Income: {income}")
print(f"Fixed Expenses: {total_fixed}")
print(f"Variable Expenses: {total_variable}")
print(f"Total Monthly Expenses: {total_expenses}")
print(f"\nSavings Potential: {monthly_savings}")
print(f"Savings Rate: {savings_rate:.2f}%")
print(f"Current Vacation Fund: {current_fund}")
print(f"Projected Fund in {months} months: {projected_fund}")
print(f"\nVacation Target: {vacation_cost}")
print(f"Total Needed: {total_needed}")
print(f"Monthly Needed: {monthly_needed:.2f}")
print(f"Monthly Shortfall/Surplus: {monthly_gap:.2f}")
print(f"Total Gap at Vacation Date: {total_gap}")
print("\n--- Financial Health Indicators ---")
print(f"Emergency Status (<10%): {emergency_status}")
print(f"Needs Improvement (10-14%): {needs_improvement}")
print(f"Stable (15-24%): {stable}")
print(f"Strong (>=25%): {strong}")
print(f"Vacation Affordable: {vacation_affordable}")
