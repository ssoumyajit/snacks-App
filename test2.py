import csv

file_name = "snacks1.csv"
try:
    #csvfile = open(file_name, 'rt')
    csvfile = open(file_name, newline='')
except:
    print("File not found")
csvReader = csv.reader(csvfile, delimiter=",")
l =  list()
#print(l)




'''
e_data = []
#name = []
for row in csvReader:
    print(row)
    #print(row[0])
    #name.append(row[0])
    #print("row is : ", row)
    dt=[]
    new_outtime = None
    for i in range(0,len(row)):
      if i % 2 == 1:
        new_outtime = (int(row[i]),int(row[i+1]))
        #print(new_outtime)
        dt.append(new_outtime)
        #print(dt) 
        
      else:
        pass
    if dt != []:
        e_data.append(dt)

#print(name)
#print(e_data)
'''






    #l.append(tuple(row))
    #l.append((row[0], row[1], row[2], row[3]))
#print(l)



'''
import csv
from pprint import pprint

with open('snacks1.csv', newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))

pprint(res)
'''

        