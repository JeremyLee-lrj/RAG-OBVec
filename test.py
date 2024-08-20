import pymysql

conn = pymysql.connect(host="10.100.2.242", port=2880,
			user="root", db="test")

cur = conn.cursor()

try:
	sql = 'drop table if exists cities'
	cur.execute(sql)

	sql = 'create table cities(id int, name varchar(24), vec vector(3))'
	cur.execute(sql)

	sql = "insert into cities values(1, 'hangzhou', '[1, 2, 5]'), (2, 'shanghai', '[1, 2, 3]')"
	cur.execute(sql)
	
	sql = 'select * from cities'
	cur.execute(sql)
	ans = cur.fetchall()
	print(ans)
	
	sql = 'create vector index vidx on cities(vec vector_l2_ops) with(type=hnsw)'
	cur.execute(sql)
	
	sql = "select * from cities order by l2_distance(vec, '[1, 2, 1]')"
	cur.execute(sql)
	res = cur.fetchall()
	for c in res:
		print(c)

finally:
	cur.close()
	conn.close()
