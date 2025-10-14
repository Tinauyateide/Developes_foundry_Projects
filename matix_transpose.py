import numpy as np  

x = np.array([1,2,3,4],
     [5,6,7,8],
     [9,10,11,12])

def thinker(x):
    trans = []
    for i in range(len(x[0])):
        new_row = []
        for row in x:
            new_row.append(row[i])
        trans.append(new_row)
    return trans

print(thinker(x))