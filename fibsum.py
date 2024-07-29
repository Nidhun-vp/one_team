first=1
second=1
i,sum=0,0
next=0
list=[]
limit=int(input("enter limit:"))
while(i<limit):
    list.append(first)
    next=first+second
    sum=sum+first
    first=second
    second=next
    i=i+1
print(list)    
print("sum of up to n is:",sum)    