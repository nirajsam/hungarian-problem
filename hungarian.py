

swimmers=['carl', 'chris', 'david', 'tony', 'ken']
jobs=['backstroke', 'breaststroke', 'butterfly', 'freestyle','dummy']

# time Matrix
time=[[37.7,32.9,33.8,1000,35.4],
      [33.1,1000,42.2,34.7,41.8],
      [33.3,38.9,28.5,30.4,33.6],
      [29.2,26.4,29.6,28.5,1000],
      [0,0,0,0,0]]
# time=[[10,14,22,12],
#       [16,10,18,12],
#       [8,14,20,14],
#       [20,8,16,6]]
n = 5
RealTime = []
for x in range(n):
        p=[]
        for y in range(n):
            p.append(time[x][y]);
        RealTime.append(p)
# 1 find minimum of all row time
minRow = []
for x in range(n):
    t = time[x][0]
    for y in range(n):
        if(time[x][y]<t):
            t = time[x][y]
    minRow.append(t)

# 2 subtract min of each row time from all row elements
for x in range(n):
    for y in range(n):
        time[x][y] = time[x][y] - minRow[x]


# 3 subtract min of each column time from all column elements
minColumn = []
for x in range(n):
    t = time[0][x]
    for y in range(n):
        if(time[y][x]<t):
            t = time[y][x]
    minColumn.append(t)


for x in range(n):
    for y in range(n):
        time[y][x] = time[y][x] - minColumn[x]

def HungarianSolution(time):
    # step 4 Assigning zero and crossed
    #copy main array into another array time2
    time2 =[]
    for x in range(n):
        p=[]
        for y in range(n):
            p.append(time[x][y]);
        time2.append(p)
     
    x=0
    while(x<n):
        count=0
        for y in range(n):
            if(time2[x][y] == 0 and count == 0):
                time2[x][y] = 'A'
                count+=1
                for i in range(1,n):
                    if(time2[i][y] == 0):
                        time2[i][y] = 'C'
            elif(time2[x][y] == 0 and count != 0):
                time2[x][y] = 'C'
        x+=1
        
    countZero = 0
    rowMarkNotEncircled = []
    totalTime = 0
    swimmerStroke={}
    for x in range(n):
        for y in range(n):
            if(time2[x][y] =='A'):
                countZero+=1
                totalTime+=RealTime[x][y]
                swimmerStroke[swimmers[x]] = jobs[y]

    if(countZero == n):
        # return totalTime
        return {'totalMinTime': totalTime, 'data': swimmerStroke}
    # Step 5---mark rows that does not have encircled 0, mark column that have crossed zero in crossed 0 in marked, mark rows that have
    #encircled 0 in marked columns
    for x in range(n):
        for y in range(n):
            if(time2[x][y] =='A'):
                break
        else:
            #mark rows that does not have encircled 0
            rowMarkNotEncircled.append(x)
    columnMarkCrossedZeroMarkedRow = []
    for x in rowMarkNotEncircled:
        for y in range(n):
            if(time2[x][y]=='C'):
                columnMarkCrossedZeroMarkedRow.append(y)

    rowEncircledZeroInMarkedColumn = []
    for x in range(n):
        for y in columnMarkCrossedZeroMarkedRow:
            if(time2[x][y] == 'A'):
                rowEncircledZeroInMarkedColumn.append(x)

    print(rowMarkNotEncircled, columnMarkCrossedZeroMarkedRow, rowEncircledZeroInMarkedColumn)
    print("row",rowMarkNotEncircled, rowEncircledZeroInMarkedColumn)
    print("column",columnMarkCrossedZeroMarkedRow)
    #draw lines on all row except marked row
    #draw lines on marked row

    #Step 6--- find smallest time element not covered by lines
    Array = []
    for x in range(n):
        for y in range(n):
            if((x in rowMarkNotEncircled or x in rowEncircledZeroInMarkedColumn) and y not in columnMarkCrossedZeroMarkedRow):
                if(type(time2[x][y])!= str):
                    Array.append(time2[x][y])
    print("minArray",Array)
    smallestTime = min(Array)
    #Step 6---2 subtract this smallest from all uncovered elements
    for x in range(n):  
        for y in range(n):
            if((x in rowMarkNotEncircled or x in rowEncircledZeroInMarkedColumn) and y not in columnMarkCrossedZeroMarkedRow):
                time[x][y]-=smallestTime
    
    return HungarianSolution(time)

#step 7 
print(HungarianSolution(time))

