import csv

file = open("./write.csv", "w")
# writer = csv.writer(file)

writer = csv.writer(
    file, 
    quoting=csv.QUOTE_ALL, 
    delimiter=':',
    quotechar='`'
)
# row = ("python","-","izm","1")
# writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
print(rows)
writer.writerows(rows)

file.close()