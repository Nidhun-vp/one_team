num=int(input())
org=num
count=len(str(num))
result=0
while(num>0):
    digit=num%10
    result=result+digit**count
    num=num//10
if result==org:
    print("armstrong")
else:
    print("Not armstrong")        
    