import csv

students = open("Student_Scores.csv", "r")
outfile = open("student_avg.csv", "w")

student_file = csv.reader(students, delimiter=",")

next(student_file)

for record in student_file:
    average = (int(record[1]) + int(record[2]) + int(record[3])) / 3
    average = str("{:.2f}".format(average))
    outfile.write(record[0] + ", " + average + "\n")
