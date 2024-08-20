import json
import pymysql

with open("D:/Download/OB_text_embeddings.json", "r", encoding="utf-8") as file:
    textData_embeddings = json.load(file)

with open("data", "r", encoding='utf-8') as file:
    text = file.read()
textData = text.split(sep="\n")

Len = len(textData_embeddings)
print(Len, type(textData_embeddings))
print(len(textData), type(textData))
# test_list = [i for i in range(10)]
# print(test_list)
# print((textData_embeddings[0]))
# sql = "insert into docs values(i, %s, %s))" % (textData[0], str(textData_embeddings[0]))
# print(sql)

# exit()

conn = pymysql.connect(host="10.100.2.242", port=2880, user="root", db="test")
cur = conn.cursor()

try:
    sql = 'drop table if exists docs'
    cur.execute(sql)

    sql = 'create table docs(id int, text varchar(10000), vec vector(384))'
    cur.execute(sql)

    for i in range(Len):
        sql = "insert into docs values(%d, '%s', '%s')" % (i, textData[i], str(textData_embeddings[i]))
        cur.execute(sql)

    sql = 'create vector index vidx on docs(vec vector_l2_ops) with(type=hnsw)'
    cur.execute(sql)
    #
    sql = "select * from docs order by l2_distance(vec, '%s') limit 0, 5" % str(textData_embeddings[0])
    cur.execute(sql)
    res = cur.fetchall()
    for c in res:
        print(c)

finally:
    cur.close()
    conn.close()
