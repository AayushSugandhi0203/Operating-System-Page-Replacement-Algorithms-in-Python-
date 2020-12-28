import threading
import time

lock = threading.Semaphore()
def replacement(j,k):
#for j in range(0,len(frames)):
    lock.acquire()
    count = 0
    top = 0
    print("Printing for frame no.",k)
    table = []
    faults = 0
    for i in range(0,k):
        table.append(-1)
        
    for i in pages:
        count = count + 1
        if i not in table:
            faults = faults + 1
            table[top] = i
            top = (top+1)%k
        
                
            
        if count%N==0:    
            print("At snapshot time=",count)
            print("Table is",table)
            print("No. of Faults are",faults)
            print(" ")
    lock.release()        
print("Enter the pages with space seperation with -1 to terminate")
pages = list(map(int,input().strip().split()))
print(pages)
print("Enter the frames with space seperation with -1 to terminate")

frames = list(map(int,input().strip().split()))
print(frames)
frames.pop()
pages.pop()
print("Enter the time after which you need snapshot")
N = int(input())                    
for i in range(0,len(frames)):
    tr = threading.Thread(target = replacement , name = "Frame no. "+ str(i), args=(i,frames[i],))        
        
        
    
