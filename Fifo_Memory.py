import threading
import time

print("Enter the no. of Physical Memory pages")
p = int(input())
print("Enter the no. of Processes")
N = int(input())

print("Enter the pages for all of virtual process with space seperation")
virtual_pages = list(map(int,input().strip().split()))
print(virtual_pages)
top= 0
table = []
faults = [0]*N
hits = [0]*N
Ratio = [0]*N
for i in range(0,p):
    table.append(-1)
while(1):
    print("Enter the process id and virtual page number")    
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    x = (a,b)   
    if b > virtual_pages[a] or a>N:
        print("Invalid Input") 
    elif a==-1 and b==-1:
        break
    else:
        if x not in table:
            faults[a] = faults[a] + 1
            table[top] = x
            top = (top+1)%p
        else:
            hits[a] = hits[a] + 1
        print("Table is",table)
        print("No. of Faults are",faults)
        print("No. of Hits are",hits)
        print(" ")
    for i in range(0,N):
        if hits[i]!=0 and faults[i]!=0:
            Ratio[i] = hits[i]/(hits[i]+faults[i])
        
    print("Hit Ratio ",Ratio)
            
print("Final Hit Ratio",sum(Ratio)/N)    
                    
        
        
        
    
