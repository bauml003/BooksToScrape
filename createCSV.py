import csv

with open('output.csv', mode='w') as file:
    fieldnames = ['name', 'salary']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for data in data_to_load:
        writer.writerow(data)