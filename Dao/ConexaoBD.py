import psycopg2

con = psycopg2.connect(host='localhost', database='atlas', user='postgres', password='123456')

cur = con.cursor()
#sql = "select * from usuario"
#cur.execute(sql)
#con.commit()
cur.execute('select * from usuario')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()