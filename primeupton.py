
lower=1
limit=int(input("enter limit:"))
for num in range(lower,limit+1):
    if num>1:
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if(is_prime):
                print(num)
            
                
