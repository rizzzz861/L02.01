student = {
    "name": "Илья",
    "age": 22,
    "course": 3
}
print(student)

dict1 = {"name": "Илья", "age": 22}
dict2 = {"course": 3, "university": "МГУ"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

key = "age"
if key in student:
    print(f"Ключ '{key}' присутствует в словаре.")
else:
    print(f"Ключ '{key}' отсутствует в словаре.")
