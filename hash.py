'''
ハッシュ化は
・文字列を固定帳のサイズに変換し安全に保存することができる（データベース保存前にhash化する）
・Pythonでは辞書型のハッシュテーブルを作成するのでキーで検索可能

'''
# string = "paiza-ism"
# # hash関数による文字列のhash化
# hash_value = hash(string)
# hash_value2 = hash(string)

# print(string)
# print(hash_value)
# print(hash_value2)

import hashlib

string = "paiza-izm"

# SHA-1アルゴリズムでハッシュ化(160bit)
hash_object = hashlib.sha1(string.encode())
print(hash_object.hexdigest())

# MD-5アルゴリズムでハッシュ化(128bit)
hash_object = hashlib.md5(string.encode())
print(hash_object.hexdigest())
