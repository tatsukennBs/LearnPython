# N（要素数） K（検索文字列）が与えられる。
# そののちに配列が渡されるのでその中に存在するKの数を出力する

input_line = input()
input_list = input_line.split(" ")
print(input_list[0])
print(type(int(input_list[0])))

# 要素数分、inputを取得する。
# 取得した値とKの値を比較する。
# Kの値を一致したらcountアップする。
# 最終的にcountを出力する。

loopcount = 0
count = 0

while loopcount < int(input_list[0]):
    input_str = input()
    print(input_str)
    # 整数Kの値と取得した値が一致したらcountupする。
    if int(input_str) == int(input_list[1]):
        count += 1
    loopcount += 1

print(count)

print("======別回答")
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for i in a:
    if i == k:
        ans += 1

print(ans)