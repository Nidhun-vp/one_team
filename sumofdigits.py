rev=0
num=int(input('enter number:'))
org=num
sum=0
digit=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum of adjacent digits:",sum)        