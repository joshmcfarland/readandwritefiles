import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

next(employee_file)

for record in employee_file:
    print("Fname :", record[1])
    print("Lname :", record[2])
    salary = float(record[3])
    print("Salary: ", "${:,.2f}".format(salary))
    bonus = float(record[3]) * (float(record[4]))
    print("Bonus : ", "${:,.2f}".format(bonus))
    total_pay = salary + bonus
    print("Total Pay: ", "${:,.2f}".format(total_pay))
    input()
