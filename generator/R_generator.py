#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author:	5-Fishes
# Created on:
###### Sun Oct 10 23:46:23 PDT 2021
# Last modify on:
###### Sun Oct 10 23:46:25 PDT 2021
# Purpose: 
# Used to generator an reword json config file
# the Coordinate system for a N row x M colum gridword words works as 
# the Bottom left is (0,0), Top right is (M, N)


import json
import sys

sys.path.append("../")
from convert import Convert

M = int(input("please input the colum number:"))
N = int(input("please input the row number:"))

R = {}
for y in range(N):
    for x in range(M):
        R[Convert.coo2str(x,y)] = 0

print(R)

while True:
    inputStr = input("x y reward. (input 'e' to finish input)")

    if inputStr == 'e':
        break

    arr = inputStr.split()
    
    x = int(arr[0])
    y = int(arr[1])
    value = int(arr[2])

    R[Convert.coo2str(x,y)] = value

with open("R.json", "w") as f:
    json.dump(R, f)