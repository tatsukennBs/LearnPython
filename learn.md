# パッケージ、モジュールの考え方
- パッケージ・・・ファイルシステムでいうディレクトリ
- モジュール・・・ファイルシステムでいうファイル

# インポート文の書き方

### from パッケージ import モジュール
```
from mypack1.mypack2 import mymod
mymod.myfunc()
```

### from [パッケージ.]モジュール import 識別子（関数名）
```
from mypack1.mypack2.mymod import myfunc
myfunc()
```

# json関連
- json.dumps: dump(吐き出す)してdict→json
- ダンプ：見たい内容をファイルとかに「ぐへぇ（－Ｏ－）＝３」と吐き出すこと
- json.loads: loadするのでjson→dict

# 文字コード関連
```
非ASCII文字
アクセント記号などの付いた文字や、ギリシャ文字、キリル文字などラテン文字以外のアルファベット、漢字、仮名、ハングル、タイ文字など非欧米圏の文字、いわゆる全角英数字、全角記号、ローマ数字、顔文字などはASCII文字には含まれない。

文字コードのお話
https://qiita.com/yuji38kwmt/items/b3a7820b4d3b544da4ff
```