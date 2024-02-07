import datetime

class Testclass():
    
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def sample_classmethod(cls, date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        # このクラスのインスタンスを作成している 
        return cls(d.year, d.month, d.day)

# インスタンス作成せずに呼び出し
test_class1 = Testclass.sample_classmethod()
print(test_class1.year, test_class1.month, test_class1.day)

# インスタンス作成せずに呼び出し
test_class2 = Testclass.sample_classmethod(-15)
print(test_class2.year, test_class2.month, test_class2.day)

# インスタンス作成
test_class3 = Testclass(2000,1,1)
print(test_class3.year, test_class3.month, test_class3.day)



