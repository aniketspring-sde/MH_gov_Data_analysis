import csv
from matplotlib import pyplot as plt


REGISTRATION_DATE = "CompanyRegistrationdate_date"


def calculate(companies_file):
    year_count = {}

    with open(companies_file, "r") as companies_data:
        companies_reader = csv.DictReader(companies_data)

        for company in companies_reader:
            registration_date = company[REGISTRATION_DATE]

            if registration_date != "":
                year = registration_date[0:4]

                if year not in year_count:
                    year_count[year] = 0

                year_count[year] += 1

    year_count = dict(sorted(year_count.items()))

    return year_count


def plot(year_count):
    plt.figure(figsize=(30, 5))

    plt.bar(year_count.keys(), year_count.values())

    plt.xticks(rotation=90)
    plt.xlabel("Registration Year")
    plt.ylabel("Number of Companies")
    plt.title("Number of Companies Registered Each Year")

    plt.tight_layout()
    plt.savefig("../plots/q2_companies_registered_each_year.png")
    plt.show()


def execute():
    companies_file = "../data/maharastra_gov.csv"

    year_count = calculate(companies_file)

    plot(year_count)

    return year_count


execute()