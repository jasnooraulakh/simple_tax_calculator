import matplotlib.pyplot as plt


class TaxCalculator:

    def __init__(self):
        self.income = 0.00
        self.tax_amount = 0.00
        self.net_income = 0.00
        self.taxpayer_type = ""

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
            self.taxpayer_type = input("Enter taxpayer (Single or Married): ")

            if self.taxpayer_type.lower() == "married":
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

            elif self.taxpayer_type.lower() == "single":
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
        self.net_income = self.income - self.tax_amount
        return self.tax_amount, self.net_income

    def display_pie_chart(self):
        """Display a pie chart to visualize income breakdown"""

        plt.style.use("fivethirtyeight")

        # PIE CHART DATA:
        # Slices:
        # (tot income = 100%)
        #     Slice 1: tot income - tax amount -- "Net Income"
        #     Slice 2: tax amount -- "Taxed Income"
        slices = [self.net_income, self.tax_amount]
        labels = [f"Net Income: \n${self.net_income}", f"Tax Amount: \n${self.tax_amount}"]
        colors = ['cyan', 'red']

        # PIE CHART PARAMETERS:
        # Edge Color: Black
        plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

        plt.title(f"Gross Income Breakdown: {self.taxpayer_type.title()} Taxpayer")
        plt.tight_layout()
        plt.show()

    def donut_chart(self):

        # Outer shell properties
        outer_shell = [self.income]
        outer_label = ["Gross Income"]
        outer_colors = ["gold"]

        # Inner shell properties
        inner_shell = [self.net_income, self.tax_amount]
        inner_label = ["Net Income", "Tax Amount"]
        inner_colors = ["dodgerblue", "tomato"]

        fig, ax = plt.subplots()

        ax.pie(outer_shell, labels=outer_label,
               radius=1.2, colors=outer_colors, wedgeprops=dict(width=0.3, edgecolor="white"))

        ax.pie(inner_shell, labels=inner_label,
               radius=0.9, colors=inner_colors, autopct="%1.1f%%", wedgeprops=dict(width=0.3, edgecolor='white'))

        # Set aspect ratios equal
        ax.axis("equal")
        plt.show()

    def print_details(self):
        """Display the details for taxes calculated"""
        print("----------------------------------------------")
        print("Thank you for using the Tax Calculator")
        print("----------------------------------------------")
        print()
        print(f"Your total income was: ${self.income}")
        print(f"Net Income: ${self.net_income}")
        print(f"Tax Amount: ${self.tax_amount}")
