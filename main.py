from tax_calculator import TaxCalculator
from tax_graph import income_vs_tax

income = float(input("Please enter your income: "))

tax_calc = TaxCalculator(income)
total_tax_owed = tax_calc.calculate_tax()
print(f"Tax owed: {total_tax_owed}")

income_vs_tax(income, total_tax_owed)
