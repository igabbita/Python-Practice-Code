#Input: Array of Elements, Number to be searched
#Output: Number found/ not found
#Description:  Binary Search

def binsrch (arr,m,n):
    low = 0
    high= n

    while(low <= high):
        mid = (low+high)/2
        if m == mdcmdarr[mid]:
            print ("Number found at: ", str(mid+1))
            quit ()
        elif m < arr[mid]:
            high = mid -1
        elif m > arr[mid]:
            low = mid +1
    return    

arr = []
n= int(raw_input("Enter the number of array elements: "))
for i in range(0,n):
    arr.append(int(raw_input("Enter the sorted array elements: ")))
    
m=int(raw_input("Enter the number to be found: "))
binsrch(arr,m,n)

print ("Number not found")
