
class Testclass:
    
    #クラスの初期化処理（コンストラクタ的な）、selfは自身のフィールドにアクセスする時に必要なので宣言必須
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


#クラス外からインスタンス化して呼び出し
def test_class():
    class1 = Testclass(1,"suzuki",23)
    class2 = Testclass(2,"sato",24)
    class3 = Testclass(3,"tanaka",43)
    
    print(f"id:{class1.id},name:{class1.name},age:{class1.age}")
    print(f"id:{class2.id},name:{class2.name},age:{class2.age}")
    print(f"id:{class3.id},name:{class3.name},age:{class3.age}")

# 親クラス
class Car:
    def __init__(self, car_name, maker, emission):
        self.car_name = car_name
        self.maker = maker
        self.emission = emission

# 子クラス（継承）／継承する際はクラス名の後ろに（親クラス名）うを貴女つ
class MyCar(Car):
    def __init__(self, car_name, maker, emission, owner, purchase_date):
        super().__init__(car_name, maker, emission)
        self.owner = owner
        self.purchase = purchase_date

def car_test():
    car_class1 = MyCar("note", "nissan", "1500", "suzuki", "2024-01-01")
    car_class2 = MyCar("yaris", "toyota", "1800", "tanaka", "2022-06-01")
    car_class3 = MyCar("stepwagon", "honda", "2000", "yoshida", "2023-02-01")
    
    print(f"car_name:{car_class1.car_name}, maker:{car_class1.maker}, emission:{car_class1.emission}")
    print(f"car_name:{car_class2.car_name}, maker:{car_class2.maker}, emission:{car_class2.emission}")
    print(f"car_name:{car_class3.car_name}, maker:{car_class3.maker}, emission:{car_class3.emission}")

# インスタンスメソッド、クラスメソッド、スタティックメソッドの違い
class MethodTest():
    
    def __init__(self,id):
        self.id = id
    
    def sample_instancemethod(self, id):
        print(self.id)
        
def call_method():
    
    instance = MethodTest("12345")
    print(instance.sample_instancemethod("23456"))

if __name__ == '__main__':
    print("------------")
    test_class()
    print("------------")
    car_test()
    print("------------")
    call_method()