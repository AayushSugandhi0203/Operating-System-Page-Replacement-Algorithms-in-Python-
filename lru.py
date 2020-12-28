pages = list(map(int,input().strip().split()))
frames = list(map(int,input().strip().split()))
frames.pop()
pages.pop()
N = int(input())
for j in range(0,len(frames)):
    count = 0
    print("For frame no.",frames[j])
    chart = []
    faults = 0
    for i in range(0,frames[j]):
        chart.append(-1)
        
    for i in range(0,len(pages)):
        if pages[i] not in chart:
            if -1 in chart:
                chart[i] = pages[i]
            else:            
                change = []
                value = chart.copy()
                for k in pages[i-1::-1]:
                    if k in chart and k not in change:
                        change.append(k)
                        value.remove(k)
                        if len (value)==1:
                            
                            break
                chart[chart.index(value[0])]=pages[i]
                    
            faults = faults +1            
                                           
    print("Table is",chart)
    print("No. of Faults are",faults)
    print(" ")
                    
        
        
        
    
