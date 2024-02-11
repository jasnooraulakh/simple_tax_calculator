import matplotlib.pyplot as plt
from tax_calculator import TaxCalculator


def income_vs_tax(income, taxes):

    plt.plot(income, taxes, marker='o', color='b')
    plt.title("Income vs Tax Owed")
    plt.show()
