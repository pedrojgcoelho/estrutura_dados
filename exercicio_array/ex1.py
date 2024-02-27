from array import array
from re import L


#l = [["tst", 'tst'],["tst",'tet'] ]

list = [[1,2], [3,4], [5,6]]
for j in range(len(list[i])):
    list_one = []
    for i in range(len(list)): #for j in range(len(list[i])):
        list_one.append(list[i][j])    
    print(list_one)