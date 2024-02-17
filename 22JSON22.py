import json

x ={
"name":"John",
"age":30,
"married":True,
"divorced":False,
"children":("Ann","Billy"),
"pets": None,
"cars": [
{"model": "BMW 230", "mpg": 27.5},
{"model": "Ford Edge", "mpg": 24.1}
]
}
datastr=json.dumps(x)
data = json.loads(datastr)

#print(data["cars"][0]["model"]) bunları gereksiz ve usefull o yüzden aşağıdaki
#print(data["cars"][1]["model"])

for car in data["cars"]:
    print(car["model"],car["mpg"])

for child in data["children"]:
    print(child)