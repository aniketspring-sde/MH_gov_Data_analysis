import csv

from matplotlib import pyplot as plt


class Data:

    def __init__(self):
        pass

    def get_data(self):



        with open("data/maharastra_gov.csv", "r") as file:
            rows = csv.DictReader(file)

            return list(rows)





# print(Data().get_data())
