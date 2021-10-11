import json

d = [1,3,4]

with open("test.json", "w") as f:
    json.dump(d, f)