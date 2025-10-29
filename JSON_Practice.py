import json
# Write a Python program to convert JSON data to Python object
json_obj = '{"name":"kunal","lastname":"sontakke","company":"calsoft","address":"Nagpur"}'
#
pyth_obj = json.loads(json_obj)
print(pyth_obj)
print(pyth_obj['name'])
print(pyth_obj['address'])

# ======================================================================================================================
# Write a Python program to convert JSON data to Python object
# pyth_obj = {"name":"kunal","lastname":"sontakke","company":"calsoft","address":"nagpur"}

# j_data = json.dumps(pyth_obj)

# print(j_data)

# ======================================================================================================================
# Write a Python program to convert Python objects into JSON strings. Print all the values.
# python_dict = {"name": "David", "age": 6, "class":"I"}
# python_list = ["Red", "Green", "Black"]
# python_str = "Python Json"
# python_int = (1234)
# python_float = (21.34)
# python_T = (True)
# python_F = (False)
# python_N = (None)
#
# json_dict = json.dumps(python_dict)
# json_list = json.dumps(python_list)
# json_str = json.dumps(python_str)
# json_int = json.dumps(python_int)
# json_float = json.dumps(python_float)
# json_T = json.dumps(python_T)
# json_F = json.dumps(python_N)
# json_N = json.dumps(python_N)
#
# print(json_dict)
# print(json_list)
# print(json_str)
# print(json_int)
# print(json_float)
# print(json_T)
# print(json_F)
# print(json_N)

# ======================================================================================================================
# Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
import json
data = '{"name":"kunal","lastname":"sontakke"}'

json_data = json.loads(data)
print(type(json_data))

dump_data = json.dumps(data)
print(type(dump_data))

