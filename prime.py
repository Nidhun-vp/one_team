num=int(input())
i=2
while(i<num):
    if(num%i==0):
        print("the given no ",num,"is Not prime")
        break
    else:
        i=i+1 
        print("the given no:",num,"is prime")   
        break
print("success")    
