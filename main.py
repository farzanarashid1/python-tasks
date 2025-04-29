import requests
import csv
import pandas
url = "https://clinicaltrials.gov/"
res = requests.get(url)
file = "clinic.csv"
if res.status_code==200:
    data = res.text
    f = open(file, 'w')
    for i in data:
        f.write(i)


        # x = csv.writer(f)
        # x.writerow(i)

    # d = pandas.read_csv("clinic.csv")
    # print(d)
else:
    print("permission denied")

f1 = open("clinic.csv",'r')
print(f1.read())
