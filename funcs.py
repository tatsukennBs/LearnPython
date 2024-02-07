# 引数指定あり関数
def func_tests_main(n1,n2,oper):
    if oper == 1:
        print(n1 + n2)
    elif oper == 2:
        print(n1 - n2)
    elif oper == 3:
        print(n1 * n2)
    elif oper == 4:
        print(n1 / n2)

# 引数指定あり関数（初期値あり）
def func_tests_main2(n1,n2,oper=1):
    if oper == 1:
        print(n1 + n2)
    elif oper == 2:
        print(n1 - n2)
    elif oper == 3:
        print(n1 * n2)
    elif oper == 4:
        print(n1 / n2)

# 可変長引数
def func_tests_main_args(count, *args):
    print(count)
    print(args)

# 可変長引数(辞書で渡す/keywords arguments)
def func_tests_main_args2(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    func_tests_main(200,100,4)
    print("------------")
    # 引数省略の場合は設定した初期値が代入される
    func_tests_main2(200,100)
    print("------------")
    # 可変長引数はタプルで渡される
    func_tests_main_args(2,"blue","red","green")
    # 可変長引数はタプルで渡される
    func_tests_main_args2(id=1, value=12345)