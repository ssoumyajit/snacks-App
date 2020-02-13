#this script reads the csv data and ouputs like below
#demo_employee_data = [{'r1':[(525,529),(670,700)]},{'r2':[(530,534),(680710)]}] - now in this format

import csv

file_name = "snacks1.csv"
try:
    #csvfile = open(file_name, 'rt')
    csvfile = open(file_name, newline='')
except:
    print("File not found")
csvReader = csv.reader(csvfile, delimiter=",")
# reads csv data and outputs lists : row = ['r1', '1', '2','3','4']
                                   # row = ['r2', '5', '6','7','8']

demo_employee_data = []
for row in csvReader:
    outtimes = []

    for i in range(0,len(row)):
        if i % 2 == 1:
            new_outtime = (int(row[i]),int(row[i+1]))
            outtimes.append(new_outtime)
            #print(outtimes)
        else:
            pass
    
    ld = {row[0]:outtimes}
    print(ld)
    demo_employee_data.append(ld)
#print(demo_employee_data)

