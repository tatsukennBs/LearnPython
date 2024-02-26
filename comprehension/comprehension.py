# 内包表記の基本形（リスト型）
comp_list = [i*10 for i in range(10)]
print(comp_list)

# 内包表記の基本形（辞書型(dict型)）
comp_dict = {str(i):i*15 for i in range(10)}
print(comp_dict)

# 内包表記の基本形（set型）
comp_set = {str(i*10) for i in range(10)}
print("set:{0}".format(comp_set))

# タプルの内包表記はなし