def output_test():

    # デフォルトは改行が入るが、改行せずに指定した文字を指定する
    print('python', end=' ')
    print('-', end=' ')
    print('izm', end=' ')
    print('com')
    
    # フォーマット出力する(文字列、数値)
    print("問題１の回答:%s" % "answer1")
    print("問題２の回答:%s,%s,%s" % ("answers1","answers2","answers3"))
    print("%d日目" % 123)

    # フォーマット出力する(文字列、数値)／別の記法
    print("問題１の回答:{}".format("answer1"))
    print("問題２の回答:{0},{1},{2}".format("answers1","answers2","answers3"))
    print("{0}日目".format(123))

if __name__ ==  '__main__' :
    output_test()