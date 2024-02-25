
def looptest():
    
    for_test = ['python', '-', 'izm', '.', 'com']
    
    # inの左側に変数、右側に繰り返しを行う対象のオブジェクトを指定する
    for value in for_test:
        print(value)
    
    for_test2 = "Suzuki"
    
    # 文字列も対象にできる
    for value in for_test2:
        print(value)
    
    print("--------------------------------")
    
    # while文によるループ処理
    count = 0
    while count < 10:
        count += 1
        print(count)
    
    print("--------------------------------")
    
    # break処理（ループを抜ける）
    count2 = 0
    while count2 < 100:
        count2 += 1
        print(count2)
        
        if(count2 == 10):
            break
    
    print("--------------------------------")
    
    # continue処理（ループを継続）
    count3 = 0
    while count3 < 45:
        count3 += 1

        if(count3 % 10):
            continue
        
        print(count3)
    
    print("--------------------------------")
    
    # rangeの使用方法(i=0; i<10; i++と同義）
    for i in range(10):
        print(i)
    
    print("--------------------------------")
        
    # rangeの使用方法(i=3; i<8; i++と同義）/3,4,5,6,7
    for i in range(3,8):
        print(i)

if __name__ == '__main__':
    looptest()