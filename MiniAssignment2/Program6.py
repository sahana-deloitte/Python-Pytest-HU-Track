a_dict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
new_key = 'location'
old_key = 'city'
a_dict[new_key] = a_dict.pop(old_key)
print(a_dict)