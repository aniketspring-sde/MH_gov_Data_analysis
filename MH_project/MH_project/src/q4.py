from src.data import Data
import matplotlib.pyplot as plt
import  numpy as np


class Q4:
    def __init__(self):
        self.activity_count_year = {}



    def count_year(self,rows):


        for row in rows:
            activity = row['CompanyIndustrialClassification']
            year = (row['CompanyRegistrationdate_date'][:4])

            if activity not in self.activity_count_year:
                self.activity_count_year[activity] = {}

            if year not in self.activity_count_year[activity]:
                self.activity_count_year[activity][year] = 0

            self.activity_count_year[activity][year] += 1


    def plot(self):

        top5 = sorted(
            self.activity_count_year.items(),
            key=lambda x: sum(x[1].values()),
            reverse=True
        )[:5]


        years = sorted({
            year
            for _, year_dict in top5
            for year in year_dict
        })[-10:]

        x = np.arange(len(years))
        width = 0.1

        fig, ax = plt.subplots(figsize=(15, 6))

        for i, (activity, year_dict) in enumerate(top5):
            counts = []

            for year in years:
                counts.append(year_dict.get(year, 0))

            ax.bar(
                x + i * width,
                counts,
                width,
                label=activity
            )

        ax.set_xticks(x + width * 2)
        ax.set_xticklabels(years)

        ax.set_xlabel("Year")
        ax.set_ylabel("Registration Count")
        ax.set_title("Top 5 Principal Business Activities (Last 10 Years)")
        ax.legend()

        plt.tight_layout()
        plt.show()


    def execute(self,rows):
        self.count_year(rows)
        self.plot()
