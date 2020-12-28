

print("Enter the pages with space seperation")
pages = list(map(int,input().strip().split()))
print(pages)
print("Enter the frames with space seperation")

frames = list(map(int,input().strip().split()))
print(frames)
frames.pop()
pages.pop()
print("Enter the time after which you need snapshot")
N = int(input())
for j in range(0,len(frames)):
    count = 0
    top = 0
    where_to_put = [None for i in range(frames[j])]
    print("Printing for frame no.",frames[j])
    table = []
    faults = 0
    for i in range(0,frames[j]):
        table.append(-1)
        
    for i in range(0,len(pages)):
        count = count + 1
        flag = 0
        x = i
        
        if pages[i] not in table:
            if -1 in table:
                table[i] = pages[i]
            else:    
                for k in range(0,len(table)):
                    if table[k] not in pages[i+1:]:
                        table[k] = pages[i]
                        flag = 1
                        break
                if flag==0:
                        i = x
                        for k in range(0,len(table)):
                        
                            if table[k] in pages[i+1:]:
                                where_to_put[k] = pages[i+1:].index(table[k])    
                if flag==0:
                    table[where_to_put.index(max(where_to_put))] = pages[i]
            faults = faults + 1
                
                
            
        if count%N==0:    
            print("At snapshot time=",count)
            print("Table is",table)
            print("No. of Faults are",faults)
            print(" ")
                    
        
        
        
    
