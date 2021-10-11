import json
import sys

sys.path.append("../")
from convert import Convert

A = [[0,0], [0,1], [0,-1], [-1,0], [1,0]]
#   No Move  Up     Down    Left    Right

def step(x, y, a, M, N):
    nx = x + A[a][0]
    ny = y + A[a][1]

    xyStr = Convert.coo2str(x,y)

    if nx < 0 or nx >= M:
        return xyStr
    if ny < 0 or ny >= N:
        return xyStr
    if GW[Convert.coo2str(nx,ny)] == 0:
        return xyStr
    return Convert.coo2str(nx,ny)
    


# build an initial P
M = int(input("please input the colum number: "))
N = int(input("please input the row number: "))

P = {}

for y in range(N):
    for x in range(M):
        P[Convert.coo2str(x,y)] = {}
        for k in range(5):
            P[Convert.coo2str(x,y)][k] = {}
            for j in range(N):
                for i in range(M):
                    P[Convert.coo2str(x,y)][k][Convert.coo2str(i,j)] = 0

GW = {}

with open("GW.json", "r") as f:
    GW = json.load(f)

err = float(input("please input the err rate: "))

suc = 1-err
err = err/4

for y in range(N):
    for x in range(M):
        for k in range(5):
            for j in range(5):
                if j == k:
                    P[Convert.coo2str(x,y)][k][step(x,y,j,M,N)] += suc
                else:
                    P[Convert.coo2str(x,y)][k][step(x,y,j,M,N)] += err

print(P[Convert.coo2str(3,3)][0])
print(P[Convert.coo2str(3,3)][1])
print(P[Convert.coo2str(3,3)][3])