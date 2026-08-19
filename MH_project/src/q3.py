import csv
from matplotlib import pyplot as plt


REGISTRATION_DATE = "CompanyRegistrationdate_date"
REGISTERED_ADDRESS = "Registered_Office_Address"
ZIPCODE = "zipcode"
DISTRICT = "district"


def calculate(companies_file, zipcode_file):
    zipcode_to_district = {}

    with open(zipcode_file, "r", newline="", encoding="utf-8") as zipcode_data:
        zipcode_reader = csv.DictReader(zipcode_data)

        for zipcode_row in zipcode_reader:
            zipcode_to_district[zipcode_row[ZIPCODE]] = zipcode_row[DISTRICT]

    district_count = {}

    with open(companies_file, "r", newline="", encoding="utf-8") as companies_data:
        companies_reader = csv.DictReader(companies_data)

        for company in companies_reader:
            registration_date = company[REGISTRATION_DATE]

            if registration_date[0:4] == "2015":
                zipcode = company[REGISTERED_ADDRESS].split(",")[-1].strip()[:6]

                if zipcode in zipcode_to_district:
                    district = zipcode_to_district[zipcode]

                    if district not in district_count:
                        district_count[district] = 0

                    district_count[district] += 1

    district_count = dict(
        sorted(
            district_count.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    return district_count


def plot(district_count):
    plt.figure(figsize=(30, 5))

    plt.bar(
        district_count.keys(),
        district_count.values()
    )

    plt.xticks(rotation=90)
    plt.xlabel("District")
    plt.ylabel("Number of Companies")
    plt.title("Companies Registered in 2015 by District")

    plt.tight_layout()
    plt.savefig("../plots/q3_companies_registered_2015_by_district.png")
    plt.show()


def execute():
    companies_file = "../data/maharastra_gov.csv"
    zipcode_file = "../data/zipcode_to_district.csv"

    district_count = calculate(
        companies_file,
        zipcode_file
    )

    plot(district_count)

    return district_count


execute()