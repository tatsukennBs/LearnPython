def test():
    print("number sample start")
    
    # 四則演算は他言語と同一のため割愛

    # string → intへの変換    
    test_str = "1234567890"
    print(type(int(test_str)))
    print(int(test_str))
    
    # 浮動小数点型(float)型
    test_float = 1234567890.01234
    print(type(test_float))
    print(test_float)
    
    # 複素数（complex）型
    test_complex = 100 + 2j
    print(type(test_complex)) 
    print(test_complex)

if __name__ == '__main__':
    test()