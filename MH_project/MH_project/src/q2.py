from src.data import Data
import matplotlib.pyplot as plt


class Q2:

    def  __init__(self):

        self.year_cnt = {}

    def year_reg(self,rows):

        for row in rows:
            year = row['CompanyRegistrationdate_date'][0:4]
            if year in self.year_cnt:
                self.year_cnt[year] += 1
            else:
                self.year_cnt[year] = 1


    def plot(self):
        plt.figure(figsize=(30, 5))

        plt.bar(self.year_cnt.keys(), self.year_cnt.values())
        plt.xticks(rotation=90)
        plt.show()

    def execute(self,rows):
        self.year_reg(rows)
        self.plot()
