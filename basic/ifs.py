def iftest():
    
    value = 123
    
    # if文は特に他の言語と同様、passは処理なしの記述
    if value == 321:
        pass
    elif value == 432:
        print("valueは432")
    elif value == 123:
        print("valueは123")
    else:
        print("合致する値なし")

if __name__ == '__main__':
    iftest()