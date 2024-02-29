import os

# 改行コードの取得（os.linesepでクロスプラットフォームで改行コード取得ができる）
test_str = "python-izm.com"
print(test_str.replace(".",os.linesep))

# 環境変数の取得
for env in os.environ:
    print(env)