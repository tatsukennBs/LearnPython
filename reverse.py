python_list = []
python_list.append("python")
python_list.append("izm")
python_list.append("sample")
python_list.append("list")
python_list.append("reverse")


print("そのまま表示")
for value in python_list:
    print(value)
    
# print("****************")
# print("逆順表示")

# python_list.reverse()
# for value in python_list:
#     print(value)

print("****************")
print("逆順表示(もとのリストは変更せず)")

for value in reversed(python_list):
    print(value)

print("****************")   
print("そのまま表示（再表示）")
for value in python_list:
    print(value)

print("****************")  
print("listのidx表示(開始idxを0以外に指定)") 
for index, value in enumerate(python_list, 1):
    print(f"index:{index}, value:{value}")