class TaxCalculator:

    def __init__(self, income):
        self.income = income
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

    def calculate_tax(self):
        """Calculate the tax owed amount across brackets."""
        tax_owed = 0.00
        previous_upper = 0

        for lower_limit, upper_limit, rate in self.tax_bracket:
            if self.income > lower_limit:
                # Calculate income in the current bracket
                income_in_this_bracket = min(self.income, upper_limit) - lower_limit
                # Accumulate the tax owed for the current bracket
                tax_owed += income_in_this_bracket * rate
                previous_upper = upper_limit
            else:
                break

        self.tax_amount = tax_owed
        return self.tax_amount

