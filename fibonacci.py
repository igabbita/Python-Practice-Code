#Input: Number of iterations to be performed
#Output: Desired Fibonacci series
#Description: Fibonacci generator

n= int(raw_input("Enter the number of iterations to be performed: ")) 

if n==0:
    print ('Enter a valid number')
    quit()
    
if n==1:
    print ('0')
    quit()

if n<0:
    print("Enter a positive number")
    quit()
        
else: 
    a=0
    b=1
    print a
    print b
    for i in range (2,n):
        c= a+b
        a=b 
        b=c
        print b

