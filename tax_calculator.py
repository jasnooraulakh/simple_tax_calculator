import matplotlib.pyplot as plt
import numpy as np


class TaxCalculator:

    def __init__(self):
        self.income = 0.00
        self.tax_amount = 0.00

        self.tax_bracket = [
            (0, 11000, 0.10),
            (11001, 44725, 0.12),
            (44726, 95375, 0.22),
            (95376, 182100, 0.24),
            (182101, 231250, 0.32),
            (231251, 578125, 0.35),
            (578126, float('inf'), 0.37)
        ]

    def get_user_input(self):
        """Prompt user to enter details"""
        while True:
            taxpayer_type = input("Enter taxpayer (Single or Married): ")

            if taxpayer_type.lower() == "married":
                self.tax_bracket = [
                    (0, 22000, 0.10),
                    (22001, 89450, 0.12),
                    (89451, 190750, 0.22),
                    (190751, 364200, 0.24),
                    (364201, 462500, 0.32),
                    (462501, 693750, 0.35),
                    (693751, float('inf'), 0.37)
                ]
                break

            elif taxpayer_type.lower() == "single":
                self.tax_bracket = [
                    (0, 11000, 0.10),
                    (11001, 44725, 0.12),
                    (44726, 95375, 0.22),
                    (95376, 182100, 0.24),
                    (182101, 231250, 0.32),
                    (231251, 578125, 0.35),
                    (578126, float('inf'), 0.37)
                ]
                break

            else:
                print("Invalid entry")
                continue

        self.income = float(input("Enter your income: $"))

    def calculate_tax(self):
        """Calculate the tax owed amount across brackets"""
        tax_owed = 0.00

        for lower_limit, upper_limit, rate in self.tax_bracket:
            if self.income > lower_limit:
                # Calculate income in the current bracket
                income_in_this_bracket = min(self.income, upper_limit) - lower_limit
                # Accumulate the tax owed for the current bracket
                tax_owed += income_in_this_bracket * rate
            else:
                break

        self.tax_amount = tax_owed
        return self.tax_amount

    def display_pie_chart(self):
        """Display a pie chart to visualize income breakdown"""

        plt.style.use("fivethirtyeight")

        # PIE CHART DATA:
        # Slices:
        # (tot income = 100%)
        #     Slice 1: tot income - tax amount -- "Net Income"
        #     Slice 2: tax amount -- "Taxed Income"
        slices = [(self.income - self.tax_amount), self.tax_amount]
        labels = [f"Net Income: \n${self.income-self.tax_amount}", f"Tax Amount: \n${self.tax_amount}"]
        colors = ['cyan', 'red']

        # PIE CHART PARAMETERS:
        # Edge Color: Black
        plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

        plt.title("Gross Income Breakdown")
        plt.tight_layout()
        plt.show()
