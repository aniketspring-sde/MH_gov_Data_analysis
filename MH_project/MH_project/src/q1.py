from src.data import Data
import matplotlib.pyplot as plt



class Q1():

    def auth_cap(self,rows):
        arr = []

        for row in rows:
            if row['AuthorizedCapital'] != "":
                arr.append(int(float(row['AuthorizedCapital'])))

        return arr

    def plot(self,arr):
        bins = [0, 100000, 1000000, 10000000, 100000000, 1000000000]
        labels = ["0","<= 1L", "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
        plt.figure(figsize=(10,6))
        plt.hist(arr,bins=bins)
        plt.xscale("symlog")
        plt.xticks( bins,labels=labels)
        plt.xlabel("Authorized Capital")
        plt.ylabel("Number of companies")
        plt.title("Histogram of Authorized Capital")
        plt.tight_layout()
        plt.show()



    def execute(self,rows):
        arr = self.auth_cap(rows)
        self.plot(arr)




