#Input: Data to be entered/deleted
#Output: Operation performed
#Description: Stack Implementation

arr = []
top = -1
n = int(raw_input("Enter the total size stack: "))

def printS():
    global top
    global arr

    print "Top: " + str (top)
    print "Elements of the stack: "
    for i in reversed (range (0, top + 1)):
        print arr[i]
    print ""

def pushS(data):
    global top
    global arr
    global n
    
    if top >= n - 1:
        print "Stack Max-ed out. Cannot insert"
        return

    top = top + 1
    arr[top] = data 
    print "Data Inserted: " + str(data)
    printS()
    return

def popS():
    global top
    global arr

    if top <= -1:
        print "Stack Emptied out. Cannot pop"
        return
    
    temp = arr [top]
    top = top-1
    print "Data Deleted: " + str(temp)
    printS()
    return temp
    
arr = [None]* n
while (True):
    op =int(raw_input("Enter the operation to be performed: \n 1 for Push \n 2 for Pop \n 3 for Print \n 4 to Exit\n"))
    if op == 1:
        data= int(raw_input("Enter the data: "))
        pushS(data)
    elif op == 2:
        popS()
    elif op == 3:
        printS()
    elif op == 4:
        quit()
    else:
        print "Invalid Input"

    






