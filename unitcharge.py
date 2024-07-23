unit=int(input())
if unit<=100:
    charge=unit*0.5
elif unit>100 and unit<=200:
    charge=50+(unit-100)*1    
elif unit>200 and unit<=300:
    charge=150+(unit-200)*1.5
else:charge=300+(unit-300)*2
print("your current bill is:",charge)
         