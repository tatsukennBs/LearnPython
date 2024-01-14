import os
import sys

def test():
    print("string sample start")
    
    # 複数行に分けて文字列を記載することができる
    test_str = """
    1行目です
    2行目です
    3行目です
    """ 
    print(test_str)
    
    # 文字列連携は+で可能（javaと同じ）
    test_str2 = "python"
    test_str2 = test_str2 + "-"
    test_str2 = test_str2 + "ism"
    print(test_str2)
    
    # *n でn回繰り返し連結可能
    test_str3 = "python:" * 5
    print(test_str3)

    # int→stringに変換    
    test_integer = 1234567890
    print(str(test_integer) + "円です")
    
    # 指定した文字で分割(javaと同じ),listで返却される
    str_list = test_str2.split("-")
    print(str_list[0])
    print(str_list[1])
    
    # 文字列が指定した任意の文字で開始されているかを調べる
    print(test_str2.startswith("python"))
    print(test_str2.startswith("java"))
    
    # 文字列に指定した任意の文字があるかを調べる
    print("py" in test_str2)
    print("thon" in test_str2)
    print("java" in test_str2)
    
    # 大文字を小文字に変換、小文字を大文字に変換
    test_str_upper = "Python-Ism.Com"
    test_str_lower = "python-ism.com"
    print(test_str_upper.lower())
    print(test_str_lower.upper())
    
    # 先頭（left）、末尾（right）を削除
    test_str_strip = "    python-ism.com     "
    print(test_str_strip.lstrip())
    print(test_str_strip.rstrip() + "/")
    test_str_strip = "python-ism.com.C"
    print(test_str_strip.lstrip("python"))
    print(test_str_strip.rstrip(".C"))
    

if __name__ == '__main__':
    test()