import csv
import json

object = open('Studentdata.csv', 'r')

data = csv.DictReader(object)
records = list(data)

object.close()  # must close!

with open("studentdata.json", "w") as file:
    json.dump(records, file, indent=4)

print("DATA is converted to JSON format")