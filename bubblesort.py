# Input: Array of integers
# Output: Sorted array of integers
# Description: Bubble sort algorithm on a list of integers

def bubbleSort (arr):
    n = len (arr)
    
    for i in range(0, n-1):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print ("Sorted Array: " + str(arr))

    
# read input parameters
arr = []
n = int(raw_input("Enter the number of elements of the array: "))
print ("Enter the elements of the array: \n")
for i in range (0, n):
    arr.append(int(raw_input()))

print ("Initial Array: " + str(arr))

bubbleSort(arr)

