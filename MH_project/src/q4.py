import csv
from matplotlib import pyplot as plt


BUSINESS_ACTIVITY = "CompanyIndustrialClassification"
REGISTRATION_DATE = "CompanyRegistrationdate_date"


def calculate(companies_file):
    activity_year_count = {}

    with open(companies_file, "r") as companies_data:
        companies_reader = csv.DictReader(companies_data)

        for company in companies_reader:
            business_activity = company[BUSINESS_ACTIVITY]
            registration_year = company[REGISTRATION_DATE][:4]

            if business_activity not in activity_year_count:
                activity_year_count[business_activity] = {}

            if registration_year not in activity_year_count[business_activity]:
                activity_year_count[business_activity][registration_year] = 0

            activity_year_count[business_activity][registration_year] += 1

    return activity_year_count


def plot(activity_year_count):
    top_5_activities = sorted(
        activity_year_count.items(),
        key=lambda activity_data: sum(activity_data[1].values()),
        reverse=True
    )[:5]

    years = set()

    for business_activity, year_count in top_5_activities:
        for year in year_count:
            years.add(year)

    years = sorted(years)[-10:]

    bar_width = 0.15

    plt.figure(figsize=(15, 6))

    for activity_number in range(len(top_5_activities)):
        business_activity = top_5_activities[activity_number][0]
        year_count = top_5_activities[activity_number][1]

        registration_counts = []

        for year in years:
            if year in year_count:
                registration_counts.append(year_count[year])
            else:
                registration_counts.append(0)

        bar_positions = []

        for year_number in range(len(years)):
            position = year_number + (activity_number * bar_width)
            bar_positions.append(position)

        plt.bar(
            bar_positions,
            registration_counts,
            bar_width,
            label=business_activity
        )

    year_positions = []

    for year_number in range(len(years)):
        position = year_number + (bar_width * 2)
        year_positions.append(position)

    plt.xticks(year_positions, years)

    plt.xlabel("Year")
    plt.ylabel("Registration Count")
    plt.title("Top 5 Principal Business Activities (Last 10 Years)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("../plots/q4_top_5_business_activities.png")
    plt.show()


def execute():
    companies_file = "../data/maharastra_gov.csv"

    activity_year_count = calculate(companies_file)

    plot(activity_year_count)

    return activity_year_count


execute()