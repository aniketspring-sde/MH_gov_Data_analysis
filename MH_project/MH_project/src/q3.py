from src.data import Data
import matplotlib.pyplot as plt


class Q3:
    def __init__(self):
        self.rows = Data().get_data()

        self.zipcode_to_district = {
                                    '414001': "Ahmednagar",
                                    '444001': "Akola",
                                    '444601': "Amravati",
                                    '431001': "Aurangabad",
                                    '401101': "Thane",
                                    '421308': "Thane",
                                    '442401': "Chandrapur",
                                    '424001': "Dhule",
                                    '421201': "Thane",
                                    '416115': "Kolhapur",
                                    '425001': "Jalgaon",
                                    '421301': "Thane",
                                    '416003': "Kolhapur",
                                    '413512': "Latur",
                                    '423203': "Nashik",
                                    '401107': "Thane",
                                    '400001': "Mumbai",
                                    '440001': "Nagpur",
                                    '431601': "Nanded",
                                    '422001': "Nashik",
                                    '431401': "Parbhani",
                                    '412303': "Pune",
                                    '411001': "Pune",
                                    '416416': "Sangli",
                                    '413001': "Solapur",
                                    '400601': "Thane",
                                    '1421002': "Thane",
                                    '401208': "Palghar",
                                    '401303': "Palghar"
                                }
        self.district_count = {}

        self.zipcode_count={}


    def reg_2015(self):
        for row in self.rows:
            zipcode = row['Registered_Office_Address'].split(',')[-1][:6]
            if (row['CompanyRegistrationdate_date'][0:4] == '2015'):
                if zipcode in self.zipcode_count:
                    self.zipcode_count[zipcode] += 1
                else:
                    self.zipcode_count[zipcode] = 1

        for zip_code, count in self.zipcode_count.items():

            if zip_code in self.zipcode_to_district:

                dist = self.zipcode_to_district[zip_code]

                if dist not in self.district_count:
                    self.district_count[dist] = 0

                self.district_count[dist] += count


        self.district_count = dict(sorted(self.district_count.items(), key=lambda item: item[1], reverse=True))




    def plot(self):
        self.reg_2015()

        plt.figure(figsize=(30, 5))

        plt.bar(self.district_count.keys(), self.district_count.values())
        plt.xticks(rotation=90)
        plt.show()



    def execute(self):
        self.reg_2015()
        self.plot()
