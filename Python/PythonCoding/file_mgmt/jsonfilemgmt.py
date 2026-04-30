import json
import os
def write_json(filename):
    data = {
        "people": [
            {"name": "john", "age": 30},
            {"name": "smith", "age":25}
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print()
