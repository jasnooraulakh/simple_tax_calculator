from tax_calculator import TaxCalculator


def intro():
    print("--------------------------------")
    print("---------TAX CALCULATOR---------")
    print("--------------------------------")
    print()
    print("What is your filing status?")
    print("1. Single")
    print("2. Married")
    print()


def get_user_input():
    tax_calc = TaxCalculator()

    # Get user's filing status
    while True:
        filing_status_input = input("Enter your input (1 or 2): ")

        if filing_status_input.isdigit() and int(filing_status_input) in [1, 2]:

            if filing_status_input == 1:
                tax_calc.taxpayer_type == "single"
            elif filing_status_input == 2:
                tax_calc.taxpayer_type == "married"
            break
        else:
            print("Invalid input")
            continue

    # Get user income
    print("Enter your income for 2023")

    while True:
        try:
            gross_income = float(input("Gross income: $"))
            if gross_income < 0:
                print("Please enter a positive value")
            else:
                tax_calc.income = gross_income
                break

        except ValueError:
            print("Invalid income")

    return tax_calc


def main():
    intro()
    get_user_input()


if __name__ == "__main__":
    main()
