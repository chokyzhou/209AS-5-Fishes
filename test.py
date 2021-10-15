from convert import Convert
import json

size = {
    'M': 5,
    'N': 5
}

with open("test.json", "w") as f:
    json.dump(size, f)