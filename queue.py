#Input: Data to be entered/deleted
#Output: Operation performed
#Description: Queue Implementation

arr = []
top = -1
low= 0
n= int(raw_input("Enter total size of the queue: \n"))

def pushq():
    global arr
    global top
    global low
    global n  
    top = top +1
    if top >= n:
        print ("Queue size exceeded, data cannot be inserted \n")
        return
    else: 
        data = arr[top]
        print("Data Inserted \n")
        printq()
    return

def popq():  
    global low
    global arr
    global top
    if low>top:   
        print("Queue already emptied!!! \n")   
        low = 0
        top =-1
        arr = []
        return
    else: 
        temp = arr [low]
        low= low+1
        top= top+1
        print("Data Deleted: " +str(temp))      
        printq()
        return    
    
def printq():
    global arr
    global top
    global low
    
    if low>top:
        print("Queue Empty , Refreshing Queue ")
     
    else:
        print ("Low= " +str(low))
        print ("Top= " +str(top))
        print ("Queue elements are: ")
        for i in range (low,top+1):
            print arr[i]

while (True):
    op=int(raw_input("Enter the desired operation: \n 1 for Insert \n 2 for Delete \n 3 for Print \n 4 for Exit \n")) 
    
    if op == 1:
        data = arr.append (int(raw_input("Enter the data: \n")))
        pushq()
    
    if op == 2:
        popq()
        
    if op == 3:
        printq()

    if op == 4:
        quit()
        



