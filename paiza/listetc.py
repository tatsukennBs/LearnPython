# ****
# 配列の合計
# ****
# # input値を取得する
# n = int(input())
# # 整数分input値を取得してlistに設定する
# input_list = [int(input()) for _ in range(n)]
# # list値の合計を出力する
# print(sum(input_list))


# ****
# 配列の最大値、最小値
# ****
# input値を取得する
# n = int(input())
# # 整数分input値を取得してlistに設定する
# input_list = [int(input()) for _ in range(n)]
# # list値の最大値を求める
# print(max(input_list))
# # list値の最小値を求める
# print(min(input_list))

# ****
# リストに指定要素が含まれるかどうかの確認
# ****
# input値を取得する
# input_line = input()
# input_list = input_line.split(" ")

# # 整数分input値を取得してlistに設定する
# item_list = [int(input()) for _ in range(int(input_list[0]))]

# checkFlg = False
# # リスト内の要素を検査
# for value in item_list:
#     if value == int(input_list[1]):
#         checkFlg = True
    
# if checkFlg == True:
#     print("Yes")
# else:
#     print("No")

print("======別回答")
n, k = map(int, input().split())
item_list = [int(input()) for _ in range(n)]

# リストに要素が含まれるかはこちらの方法で書く方がシンプルに書ける
if k in item_list:
    print("Yes")
else:
    print("No")
    