ba=int(input("enter basic_salary:"))
if ba<10000:
    da=ba*0.1
    hra=0
    pf=0
    netsalary=ba+da+hra-pf
elif ba>10000 and ba<=20000:
    da=ba*0.18
    hra=ba*0.1
    pf=ba*0.4
    netsalary=ba+da+hra-pf   
else:
    da=ba*0.15
    hra=ba*0.2
    pf=ba*0.2
    netsalary=ba+da+hra-pf     
print("Total salary is:",netsalary)    