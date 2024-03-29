from tax_calculator import TaxCalculator


def intro():
    """Print the introductory text"""
    print("--------------------------------")
    print("---------TAX ESTIMATOR----------")
    print("--------------------------------")
    print()
    print("What is your filing status?")
    print("1. Single")
    print("2. Married")
    print()


def get_user_input():
    """Get user input-set status, bracket, & income"""
    tax_calc = TaxCalculator()

    # Get user's filing status
    while True:
        filing_status_input = input("Enter your input (1 or 2): ")

        if filing_status_input.isdigit() and int(filing_status_input) in [1, 2]:
            filing_status_input = int(filing_status_input)

            # Verify and pass status to class
            if filing_status_input == 1:
                tax_calc.taxpayer_type = "single"
                tax_calc.set_tax_bracket()
            elif filing_status_input == 2:
                tax_calc.taxpayer_type = "married"
                tax_calc.set_tax_bracket()
            break
        else:
            print("Invalid input")
            continue

    # Get user income
    print("Enter your income for 2023")

    # Verify and pass income to class
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


def menu():
    """Display menu for the program"""
    print()
    print("What would you like to do?")
    print("1. Tax Details")
    print("2. Pie Chart")
    print("3. Donut Chart")
    print("4. Exit")

    while True:
        menu_input = input("Input: ")

        if menu_input.isdigit() and int(menu_input) in [1, 2, 3, 4]:
            return int(menu_input)
        else:
            print("Invalid input")


def main():
    intro()
    tax_calc = get_user_input()
    tax_calc.calculate_tax()

    while True:
        choice = menu()

        if choice == 1:
            # Display calculated tax details
            tax_calc.print_details()
        elif choice == 2:
            # Display pie chart
            tax_calc.display_pie_chart()
        elif choice == 3:
            # Display advanced pie/donut chart
            tax_calc.donut_chart()
        elif choice == 4:
            # Exit
            print()
            print("Thank you for using the Tax Estimator")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
