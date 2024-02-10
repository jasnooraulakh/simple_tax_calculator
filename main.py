from tax_calculator import TaxCalculator

income = float(input("Please enter your income: "))

tax_calc = TaxCalculator(income)
total_tax_owed = tax_calc.calculate_tax()
print(f"Tax owed: {total_tax_owed}")
