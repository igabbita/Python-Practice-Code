front=0
rear=0
arr=[]
n=int(raw_input("Enter the queue size: \n"))
arr = [None]*(n)

def pushq():
    global front
    global rear
    global arr
    global data
    if front==((rear+1)%n):
        print ("Queue is full")
    else:
        arr[rear]=data
        rear=((rear+1)%n)
        print("Data Inserted")
        printq()

def popq():
    global front
    global rear
    global arr
    if front==rear:
        print("Queue is empty")
    else:
        temp=arr[front]
        front=((front+1)%n)
        print("Data Deleted: \n , temp")
        printq()
        
def printq():
    global front
    global rear
    global arr
    print ("Front: \n", front)
    print ("Rear: \n", rear)
    print ("The array elements are: \n", arr)

while(True):    
    op= int(raw_input("Enter the operation to be performed: \n 1 for Push \n 2 for Pop \n 3 for Print \n 4 for Exit \n"))   
    if op==1:
        data= arr.append(int(raw_input("Enter the elements of the queue: \n")))
        pushq()
    elif op==2:
        popq()
    elif op==3:
        printq()
    elif op==4:
        quit()
 
    
    
    
    