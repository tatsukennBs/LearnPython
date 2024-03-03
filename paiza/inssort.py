# 要素の数を取得
n = int(input())
# 要素のリストを取得
number_list = list(map(int, input().split(" ")))

for i in range(1, len(number_list)):
    # number_listの現在の要素と1つ前の要素を比較して、現在の要素が小さかったら入れ替える
    # これを１つずつ戻って繰り返す（i=2だったら、次はi=1、i=3だったら、次はi=2、次はi=1)
    
    # 現在の数値を退避
    # print("loopi", str(i))
    
    # iの数分繰り返す(デクリメントしながら)
    for j in range(i, 0, -1):
        # print("loopj", str(j))
        if number_list[j-1] > number_list[j]:
            # print("replace")
            replace_num = number_list[j-1] #置き換えられる数字は一旦退避
            number_list[j-1] = number_list[j]
            number_list[j] = replace_num

    number_list_str = [str(i) for i in number_list]
    print(" ".join(number_list_str))

    
    
        
    