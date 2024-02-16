from tax_calculator import TaxCalculator


def intro():
    print("-------------------------------")
    print("-------TAX CALCULATOR----------")
    print("-------------------------------")
    print()
    print("What is your filing status?")
    print("1. Single")
    print("2. Married")


def get_user_input():
    tax_calc = TaxCalculator()

    while True:
        filing_status_input = input("Enter your input (1 or 2): ")

        if filing_status_input.isdigit():

            if filing_status_input == 1:
                tax_calc.taxpayer_type == "single"
            elif filing_status_input == 2:
                tax_calc.taxpayer_type == "married"
            break
        else:
            print("Invalid input")
            continue


def main():
    intro()
    get_user_input()


if __name__ == "__main__":
    main()
