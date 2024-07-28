import json

data = {
    "name": "deidreus",
    "age": 18,
    "loc": "sorsi"
}

json_string = json.dumps(data)

print(json_string)

with open('data.json', 'w') as f:
    json.dump(data, f)