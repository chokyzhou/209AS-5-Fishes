import json
import sys

sys.path.append("../")
from convert import Convert

obstacle = []

with open("obstacle.json", "r") as f:
    obstacle = json.load(f)

GW = {}
""" M = int(input("please input the colum number:"))
N = int(input("please input the row number:")) """

with open("size.json", "r") as f:
    size = json.load(f)

M = size["M"]
N = size["N"]

for y in range(N):
    for x in range(M):
        GW[Convert.coo2str(x,y)] = 1

for e in obstacle:
    GW[Convert.coo2str(e[0],e[1])] = 0

with open("GW.json", "w") as f:
    json.dump(GW,f)