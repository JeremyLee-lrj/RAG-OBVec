import json

embeddings_list = ["111", "222"]

with open("test.json", "w", encoding="utf-8") as file:
    json.dump(embeddings_list, file)
