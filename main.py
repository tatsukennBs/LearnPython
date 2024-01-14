import sys
import os

print("Hello")
# pythonの実行バージョンを表示
print(f"Version:{sys.version}")


path = os.getcwd()
print(path)

print("------------")
print("モジュールのロード")

def main():
    print("関数mainを呼び出しました")

# 別のモジュールからインポート時には実行しない
# __name__には自身から呼び出されたら__main__が代入される。
if __name__ == '__main__':
    print("python-izm")
    main()

print("------------")

# 標準入力を利用する
print("あなたの名前を教えてください")
your_name = input(">> ")

# 下記２処理は同一の意味
print(f"こんにちは！{your_name}さん！")
print("こんにちは！{}さん！".format(your_name))

