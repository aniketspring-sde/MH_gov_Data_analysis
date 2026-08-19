import csv
from matplotlib import pyplot as plt


AUTHORIZED_CAPITAL = "AuthorizedCapital"


def calculate(companies_file):
    authorized_capital = []

    with open(companies_file, "r") as companies_data:
        companies_reader = csv.DictReader(companies_data)

        for company in companies_reader:
            if company[AUTHORIZED_CAPITAL] != "":
                capital = int(float(company[AUTHORIZED_CAPITAL]))
                authorized_capital.append(capital)

    return authorized_capital


def plot(authorized_capital):
    bins = [
        0,
        100000,
        1000000,
        10000000,
        100000000,
        1000000000
    ]

    labels = [
        "0",
        "<= 1L",
        "1L to 10L",
        "10L to 1Cr",
        "1Cr to 10Cr",
        "> 10Cr"
    ]

    plt.figure(figsize=(10, 6))

    plt.hist(authorized_capital, bins=bins)

    plt.xscale("symlog")
    plt.xticks(bins, labels=labels)

    plt.xlabel("Authorized Capital")
    plt.ylabel("Number of Companies")
    plt.title("Histogram of Authorized Capital")

    plt.tight_layout()
    plt.savefig("../plots/q1_authorized_capital_histogram.png")
    plt.show()


def execute():
    companies_file = "../data/maharastra_gov.csv"

    authorized_capital = calculate(companies_file)

    plot(authorized_capital)

    return authorized_capital

execute()