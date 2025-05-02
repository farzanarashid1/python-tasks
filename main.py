# #function based
# import requests
# import csv
# import pandas
# url = "https://clinicaltrials.gov/"
# res = requests.get(url)
# file = "clinic.csv"
# def task():
#     if res.status_code==200:
#        data = res.text
#        f = open(file, 'w')
#        for i in data:
#            f.write(i)
#        # x = csv.writer(f)
#         # x.writerow(i)
#
#     # d = pandas.read_csv("clinic.csv")
#     # print(d)
#     else:
#        print("permission denied")
#
# f1 = open("clinic.csv",'r')
# print(f1.read())
#
#


# #class based
import requests
import csv
import pandas
url = "https://clinicaltrials.gov/"

file = "Djangoproj/clinic.csv"
class Task():
    def __init__(self,res):
        self.res=res
    def mytask(self):
        if self.res.status_code==200:
          data = self.res.text
          f = open(file, 'w')
          for i in data:
              f.write(i)
       # x = csv.writer(f)
        # x.writerow(i)

    # d = pandas.read_csv("clinic.csv")
    # print(d)
        else:
           print("permission denied")
res = requests.get(url)
obj = Task(res)
obj.mytask()
def read():
    f1 = open("Djangoproj/clinic.csv", 'r')
    print(f1.read())
read()
