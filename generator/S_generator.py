#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author:	5-Fishes
# Created on:
###### Sun Oct 10 23:34:14 PDT 2021
# Last modify on:
###### Sun Oct 10 23:34:16 PDT 2021
# Purpose: 
# This is a generator used to generate all sate for gridword problem states
# the Coordinate system for a N row x M colum gridword words works as 
# the Bottom left is (0,0), Top right is (M, N)

import json
import sys
sys.path.append("../")
from convert import Convert

M = int(input("please input the colum number:"))
N = int(input("please input the row number:"))

S = []

for y in range(N):
    for x in range(M):
        S.append(Convert.coo2str(x,y))

with open("S.json", "w") as f:
    json.dump(S,f)