python_list = []
python_list.append(100)
python_list.append(200)
python_list.append(25)
python_list.append(800)
python_list.append(70)

print("そのまま表示")
for value in python_list:
    print(value)

print("*******")

# print("ソートして表示（ASC）")
# python_list.sort()
# for value in python_list:
#     print(value)

# print("*******")

print("ソートして表示（ASC）（元のリストはそのまま）")
for value in sorted(python_list):
    print(value)

print("*******")  
print("そのまま表示（再表示）")
for value in python_list:
    print(value)
