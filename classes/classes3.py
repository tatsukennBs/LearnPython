import datetime

class Testclass():
    
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    # スタティック（静的）メソッド・・・インスタンス作成せずに呼び出しできるメソッド
    # デコレータとして@staticmethodをメソッド名につける
    # クラスメソッドの第１引数にはself、clsは定義しない
    @staticmethod
    def sample_staticmethod(date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return d

# インスタンス作成せずに呼び出し
test_static = Testclass.sample_staticmethod(-20)
print(test_static.year, test_static.month, test_static.day)

print(__package__)
print(__file__)
print(__name__)



