from convert import Convert
import json
p = {1: 123, 2:2345}

print(json.dumps(p))

p = json.loads(json.dumps(p))

print(p)