# パッケージ、モジュールの考え方
- パッケージ・・・ファイルシステムでいうディレクトリ
- モジュール・・・ファイルシステムでいうファイル

# インポート文の書き方

# from パッケージ import モジュール
```
from mypack1.mypack2 import mymod
mymod.myfunc()
```

# from [パッケージ.]モジュール import 識別子（関数名）
```
from mypack1.mypack2.mymod import myfunc
myfunc()
```