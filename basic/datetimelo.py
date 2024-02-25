import datetime #標準ライブラリ

def test():
    print("dateTime sample start")
    
    # 今日の日付、今日の日時を出力
    today = datetime.date.today()
    todaydetail = datetime.datetime.today()
    print(today)
    print(todaydetail)
    print(type(today))
    print(type(todaydetail))

    
    # それぞれの要素を出力
    print(today.year)
    print(today.month)
    print(today.day)
    print(todaydetail.year)
    print(todaydetail.month)
    print(todaydetail.day)
    print(todaydetail.hour)
    print(todaydetail.minute)
    print(todaydetail.second)
    print(todaydetail.microsecond)
    
    # 日付のフォーマット化
    print(todaydetail.strftime("%Y-%m-%d %H:%M:%S"))
    
    # 日付の計算（計算結果はtimedelta型）を使用
    newyear = datetime.date(2024,1,1)
    calc = today - newyear
    print(type(calc))
    print(calc.days)

if __name__ == '__main__':
    test()