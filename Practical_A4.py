n=int(input("enter the value of n: "))
if n==0:
    print("fibonacci number is:" ,0)
elif n==1:
    print("fibonacci number is:" ,1)
else:
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print("fibonacci number is:",b)
