import json
import pymysql
from pymilvus import model

ef = model.dense.SentenceTransformerEmbeddingFunction(
    model_name='all-MiniLM-L6-v2',  # Specify the model name
    device='cpu'  # Specify the device to use, e.g., 'cpu' or 'cuda:0'
)
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

    print("Please input your query:")
    while (True):
        query = input()
        if query == "exit":
            break
        query_embedding = ef.encode_documents(query)
        query_embedding = [num * 100 for num in query_embedding]
        sql = "select * from docs order by l2_distance(vec, '%s') limit 0, 10" % str(query_embedding)
        cur.execute(sql)
        res = cur.fetchall()
        for c in res:
            print(c)

finally:
    cur.close()
    conn.close()
