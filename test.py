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

