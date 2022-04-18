import pymysql

connect_db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='jing_dong', charset='utf8')

cur = connect_db.cursor()

sql_str = '''select * from goods'''

row_count = cur.execute(sql_str)
print(f'{row_count} rows in set.')
print('*' * 30)

result = cur.fetchone()
print(result)
print('*' * 30)

result = cur.fetchmany(4)
for t in result:
    print(t)
print('*' * 30)

result = cur.fetchall()
for t in result:
    print(t)
print('*' * 30)

cur.close()

connect_db.close()
