import csv

customers = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")


customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

for record in customer_file:
    print("Name:", record[1], record[2])
    print("Country:", record[4])
    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")
