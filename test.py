'''
outtime = []
row= ['r1','525','529','670','700','915','930']
for i in range(0,len(row)):
    if i == 0:
        pass
    elif i % 2 == 1:
        new_outtime = (int(row[i]),int(row[i+1]))
        outtime.append(new_outtime)
    else:
        pass
print(outtime)
'''

demo_employee_data = [{'r1':[(525,529),(670,700)]},{'r2':[(530,534),(680710)]}]

for datum in demo_employee_data:
    print(datum)
    for key in datum:
        print(key)
        print(datum[key])
        
        break
    break




