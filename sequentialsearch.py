#Input: Array of Elements, Number to be searched
#Output: Number found/ not found
#Description:  Sequential Search

def seqsrch (m,n,arr):
    for i in range(0,n-1):
        if  m== arr[i]:
            print("Number found at ", i)
            return ()    
    else:
        print ("Number not found")


arr = []
n= int(raw_input("Enter the number of array elements: "))
for i in range(0,n):
    arr.append(int(raw_input("Enter the array elements: ")))
    
m=int(raw_input("Enter the number to be found: "))
seqsrch(m,n,arr)
