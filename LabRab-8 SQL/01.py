import pymysql.cursors

conn = pymysql.connect(
    host='localhost',
    user='soft0046',
    password='vCDRap4A',
    db='soft0046_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "INSERT INTO students\
    (nameStudent, rating, gender, date, city) \
    VALUES ('Жданов', 197, 1, '2002-09-10', 'Пермь')"

count = cur.execute(sql)
conn.commit()


print(f'inserted {count} rows')

conn.close()
