import json

# json_dataは辞書型（pythonの文法上にはjson型は存在しない）
# 下記のように書いたらjson_dataの型は必然的にdict型になる。
# jsonをloadする確認をしたければ外部ファイルで定義するか。
json_data = {
  "社員": {
    "名前": "山田太郎", 
    "年齢": 28, 
    "部署": "開発部",
    "スキル": ["Java", "Python", "Go"],
    "プロジェクト": {
      "現在のプロジェクト": "システム改善プロジェクト",
      "担当部分": ["バックエンド", "データベース設計"]
    }
  }
}

print(type(json_data))

# Pythonの辞書(dict)をJSON文字列(str)に変換 json.dumps()
# 非ASCII文字はUnicodeエスケープされるのでensure_ascii=FalseをつけることでUnicodeエスケープを回避する。
# indentを指定すると要素ごとにインデント＋改行される
encoded_json_data = json.dumps(json_data, ensure_ascii=False, indent=4)
print(encoded_json_data)
print(type(encoded_json_data))

print("================================================================")

# json文字列を定義(シングルクオーテーションでくくると文字列にできる)
# s = '{"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null, NaN, Infinity]}'
s = '{"社員": {"名前": "山田太郎", "年齢": 28, "部署": "開発部","スキル": ["Java", "Python", "Go"],"プロジェクト": {"現在のプロジェクト": "システム改善プロジェクト","担当部分": ["バックエンド", "データベース設計"]}}}'

print(type(s))
# JSON文字列(str)をPythonの辞書(dict)に変換 json.loads()
d = json.loads(s)
print(d)
print(type(d))

print("================================================================")

# jsonのファイルを読み込みし辞書(dict)に変換する場合はjson.load()を使用する。 json.load()
with open("./json/input.json","r") as f:
    dict = json.load(f)

print(dict)
print(type(dict))