#converts this format [{'r1':[(525,529),(670,700)]},{'r2':[(530,534),(680710)]}] to 
# r1
# [(525,529),(670,700)]  this format ( breks the dictionary down to name and outtimes as of required format)

demo_employee_data = [{'r1':[(525,529),(670,700)]},{'r2':[(530,534),(680710)]}]

for datum in demo_employee_data:
    print(datum)
    for key in datum:
        print(key)
        print(datum[key])
        
        break
    break




