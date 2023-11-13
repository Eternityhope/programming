import sqlite3

data1, data2, data3, data4 = "", "", "", ""
row = None
con = sqlite3.connect("c:/sqlite/productDB")
cur = con.cursor()
cur.execute("SELECT * FROM productTable")

print("제품코드    제품명     가격            재고수량")
print("--------------------------------------------------------")
while (True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %4d   %5d" % (data1, data2, data3, data4))

con.close()

