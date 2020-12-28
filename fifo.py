import threading
import time

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
for j in range(0,len(frames)):
    count = 0
    top = 0
    print("Printing for frame no.",frames[j])
    table = []
    faults = 0
    for i in range(0,frames[j]):
        table.append(-1)
        
    for i in pages:
        count = count + 1
        if i not in table:
            faults = faults + 1
            table[top] = i
            top = (top+1)%frames[j]
        
                
    
            
        if count%N==0:    
            print("At snapshot time=",count)
            print("Table is",table)
            print("No. of Faults are",faults)
            print(" ")
                    
        
        
        
    
