number_list = [10,20,30,20,6,78]
number_tuple = (10,20,30,20,6,78)
number_set = {10,20,30,20,6,78}

# 最小値を取得する（リスト、タプル、セット）
print(min(number_list)) # 6
print(min(number_tuple))
print(min(number_set))

# 最大値を取得する
print(max(number_list)) # 78
print(max(number_tuple))
print(max(number_set))

# key引数を指定している場合
def key_func(n):
    return int(n)

list = [10,20,30,"100","1"]
print(min(list, key=key_func))
print(max(list, key=key_func))