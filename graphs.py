import math
grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
buildings={
            1:[],
            2:[]
        }
zeros=[]
        
for r,i in enumerate(grid):
    for c,j in enumerate(i):
        if j==1 or j==2:
            buildings[j].append([r,c])
        else:
            zeros.append([r,c])

for i in zeros:
    total = 1000000000
    new_total=0
    for j in buildings[1]:
        new_total+=abs(i[0]-j[0]) + abs(i[1]-j[1])
    total=min(total,new_total)

print(total)
print(buildings)
print(zeros)

                    
                    