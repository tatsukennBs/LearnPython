import datetime

print("array sample start")
# タプル：変更不可能（イミュータブル）なリストというイメージ、dictのキーに使用、変更を許可しない変数定義／（）で作成
# リスト：変更可能（ミュータブル）、汎用性が高い／[]で作成、appendで末尾に要素追加
# 辞書：key,valueを１つの要素として持つことができる、javaのMapと同じ／{}で作成
# セット（集合）：変更可能（要素の追加、削除が可能）、重複した要素は持つことができない／辞書と同様{}を使用する、keyなしdict


def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
    
    print(value[0])
    print(value[1])
    print(value[2])
    
def execute_list():
    
    # 空のリストを作成して末尾に要素を追加(apopend/javaだとadd)
    test_list = []
    test_list.append("python")
    test_list.append("-")
    test_list.append("izm")
    test_list.append(".")
    test_list.append("com")
    print(test_list)
    
    # インデックスを指定して要素を追加（insert)
    test_list_2 = ['python', 'izm', 'com']
    print(test_list_2)
    test_list_2.insert(1,"-") # 追加位置のインデックスを指定
    test_list_2.insert(3,".")
    print(test_list_2)

    # インデックスを指定して要素を削除（pop）
    pop = test_list_2.pop(1)
    print(pop)
    pop = test_list_2.pop(2)
    print(pop)
    # pop = test_list_2.pop() # 引数の指定なしの場合、末尾の要素が削除される
    # print(pop)
    print(test_list_2)
    print("@@@@@@@@")
    # インデックスを指定して要素を取得
    print(test_list_2[0])
    print(test_list_2[1])
    print(test_list_2[2])

    # 要素を指定して削除（最初に合致した要素を削除）（move）
    test_list_3 = ['python', '-', 'izm', '.', 'com', '.']
    test_list_3.remove("-")
    test_list_3.remove(".")
    print(test_list_3)

def execute_dict():
    test_dict_1 = {"id": 1111, "name": "suzuki", "age": 36, "sex": "male"}
    print(test_dict_1)
    
    # 辞書の取得（keyを指定して取得）
    print(test_dict_1["id"])
    print(test_dict_1.get("name"))
    
    # 辞書の取得（keyを指定して取得）／存在しないキーを指定した場合
    # print(test_dict_1["ids"])　 #getを使用しない場合はkeyErrorになる
    print(test_dict_1.get("names")) #getを使用するとNoneが返却される
    print(test_dict_1.get("names", "Key Not Found")) #返却する文字列を設定することも可能
    
    # 辞書に要素を追加（関数などはなし）
    test_dict_2 = {}
    test_dict_2["id"] = 1234
    test_dict_2["name"] = "suzuki1"
    test_dict_2["age"] = 31
    test_dict_2["sex"] = "female"
    print(test_dict_2)
    
    # 辞書から要素を削除（関数などはなし）
    del test_dict_2["age"]
    del test_dict_2["sex"]
    print(test_dict_2)
    
    # 辞書からキーのみ取得
    print(test_dict_1.keys())
    # 辞書からvalueのみ取得
    print(test_dict_1.values())
    
    # 辞書からキーとvalueを同時に取得、Goのrangeを使用したMapの取得みたい
    for key, value in test_dict_1.items():
        print(key, value)
    
    # 辞書にキーがあるかをチェックする（DynamoDBとかの存在チェックに使用可能）
    print("id" in test_dict_1)
    print("ids" in test_dict_1)

def execute_set():
    test_set1 = {1111, "suzuki", 36, "male"}
    print(test_set1)
    
    # 空のセットを使用する時はset()を使用する
    test_set2 = set()
    # セット（集合）に要素を追加する（単一の場合はadd,他のセット、リスト、タプルを使用する場合はupdateを使用）
    test_set2.add("suzuki")
    test_set2.update({"male",36,1111})
    print(test_set2)
    
    # セット（集合）から要素を削除する
    test_set2.remove("male")
    #test_set2.remove(35) #removeの場合、存在しない要素を削除しようとするとエラーとなる
    test_set2.discard(36)
    test_set2.discard(35) #discardの場合エラーとならない
    print(test_set2)
    
    # frozensetは変更不可能なセット
    test_set3 = frozenset({1111, "suzuki", 36, "male"})
    #test_set3.add("080-1234-5678") 
    #test_set3.remove(36)
    print(test_set3)
    
def execute_slice():
    test_list = ['https', 'www', 'python', 'izm', 'com']
    # スライスはシーケンスから範囲を指定して要素を取得することができる
    print(test_list[:4]) #['https', 'www', 'python', 'izm']
    print(test_list[3:]) #['izm', 'com']
    print(test_list[1:3]) #['www', 'python']
    
    # 要素の代入（置き換え）
    test_list[1:3] = ("WWW","PYTHON")
    print(test_list)
        
if __name__ == '__main__':
    get_today()
    print("------------")
    execute_list()
    print("------------")
    execute_dict()
    print("------------")
    execute_set()
    print("------------")
    execute_slice()
    
    