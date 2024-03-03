# ****
# 配列活用メニューのアイコン
#【配列を参照する操作】全ての要素に対する操作
# ****

# n,k = map(int, input().split(" "))
# item_list = [int(input()) for _ in range(n)]

# # enumerate()を使用することでlistのindexとvalueを取得できる
# for index, value in enumerate(item_list):
#     # item_list[index] = value + k
#     print(value + k)
    
# ****
# 【配列への副作用を伴う操作】条件を満たす要素のみの配列作成
# ****
# n,k = map(int, input().split(" "))
# item_list = [int(input()) for _ in range(n)]

# ans_list = []
# for value in item_list:
#     if k <= value:
#         ans_list.append(value)

# for answer in ans_list:
#     print(answer)

# ****
# STEP: 1 傾斜配点
# ****

# input値を取得する
n = int(input())

# 5科目の重み付けのlistを取得する
weight_list = input().split(" ")
for i in range(5):
    weight_list[i] = int(weight_list[i])

max_score = 0
sum_score = 0
# 生徒数分ループ
for i in range(n):
    score_list = input().split(" ")
    
    # 重み付けの点数を計算する
    for i in range(5):
        score_list[i] = int(score_list[i]) * weight_list[i]
    
    # 重み付け後の点数で合計値を算出
    sum_score = sum(score_list)

    # 合計スコアが最大スコアを上回った場合、合計スコアで上書き
    if sum_score > max_score:
        max_score = sum_score

print(max_score)