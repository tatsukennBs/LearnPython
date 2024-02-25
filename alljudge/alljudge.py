test_list1 = [100,0,200,765,452,8726]
test_list2 = ([],[],[])
print(type(test_list2))
test_list3 = (['python', 'izm', 'com'], ['www'], ['http'])
print(type(test_list3))

# 0,空のリストがある場合はfalseと判断される。リストかタプルにfalseがないかの真偽値チェックを行い１つでもfalseがあればfalseとする。
print(all(test_list1))
print(all(test_list2))
print(all(test_list3))

# リストかタプルにfalseがないかの真偽値チェックを行い１つでもtrueがあればtrueとする。
print(any(test_list1))
print(any(test_list2))
print(any(test_list3))
