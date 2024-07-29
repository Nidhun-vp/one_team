rev=0
num=int(input('enter number:'))
org=num
digit=0
while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(rev==org):
    print("palindrome")
else:
    print("not palindrome")        