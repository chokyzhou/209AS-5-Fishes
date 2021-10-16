import json

dic = {}

with open("P.json", "r") as f:
    dic = json.load(f)

for key, value in dic["(0,4)"]["1"].items():
    print(key, " : ", value)