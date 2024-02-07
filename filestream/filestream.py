import os

print(os.getcwd())

# ファイルの読み込み
f = open("./filestream/inputfile.txt","r")
for row in f:
    print(row, end="")

# ファイルの書き込み
fw = open("./filestream/inputfile.txt","w")
count = 0
while count < 10:
    fw.write("Pythonでのファイル書き込みテスト" + str(count+1) + "\n")
    count += 1

f.close()