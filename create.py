import json

data = {
    "name" : "Arthur",
    "age" : 30
}

json_string = json.dumps(data, indent=4)

print(json_string)

with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
