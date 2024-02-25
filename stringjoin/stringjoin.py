str_list = ["https://", "www", "python-izm", "com"]

# for idx, val in enumerate(str_list):
    
#     if idx == 3:
#         print(ValueError)
#     else:
#         print(val + ".", end="")

# （任意の区切り文字）.join（区切り文字を入れる要素が入ったリスト、タプル）/ .を指定
print(".".join(str_list))
# （任意の区切り文字）.join（区切り文字を入れる要素が入ったリスト、タプル）/ 改行を指定
print("\n".join(str_list))
