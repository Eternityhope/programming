import sqlite3
con = sqlite3.connect("c:/sqlite/productDB")
cur = con.cursor()
cur.execute("CREATE TABLE productTable(pcode char(5), pname char(15), price int, birthyear int)")
while(True):
    data1 = input("제품코드 ==>")
    if data1 == "":
        break
    data2 = input("제품명==>")
    data3 = input("가격==>")
    data4 = input("재고수량==>")
    sql = "INSERT INTO productTable VALUES('"+ data1 +"', '" + data2 +"', " + data3 +", " + data4 +")"
    cur.execute(sql)
con.commit()
con.close()