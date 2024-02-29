import csv

csv_file = open("./write.csv", "r", newline="")
reader = csv.reader(
    csv_file,
    dialect=csv.excel_tab # タブ文字区切りのファイル読み込み
    )


for row in reader:
    print("**************")
    for cell in row:
        print(cell)

csv_file.close()