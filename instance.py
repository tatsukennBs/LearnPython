class TestClass:
    
    def __init__(self, title):
        self.title = title

tuple_instance = ("tuple","instance")
list_instance = ["list","instance"]
dict_instance = {"1":"dict", "2":"instance"} 
class_instance = TestClass("class_instance")

python_list = []
python_list.append("python")
python_list.append("izm")
python_list.append(tuple_instance)
python_list.append(list_instance)
python_list.append(dict_instance)
python_list.append(class_instance)

for parent in python_list:
    
    # parent(リストから取り出した親要素)がタプル型かどうかをチェック
    if isinstance(parent, tuple):
        print("****tuple********")
        for child in parent:
            print(child)
            
    # parent(リストから取り出した親要素)がリスト型かどうかをチェック
    elif isinstance(parent, list):
        print("****list********")
        for child in parent:
            print(child)
            
    # parent(リストから取り出した親要素)が辞書型かどうかをチェック
    elif isinstance(parent, dict):
        print("****dict********")
        for child in parent.keys():
            print(parent[child])
            
    # parent(リストから取り出した親要素)がTestClass型かどうかをチェック
    elif isinstance(parent, TestClass):
        print("****TestClass********")
        print(parent.title)
    
    else:
        print("****string********")
        print(parent)

    
    