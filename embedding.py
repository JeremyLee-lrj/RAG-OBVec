import json

from pymilvus import model
from sentence_transformers import SentenceTransformer

ef = model.dense.SentenceTransformerEmbeddingFunction(
    model_name='all-MiniLM-L6-v2',  # Specify the model name
    device='cpu'  # Specify the device to use, e.g., 'cpu' or 'cuda:0'
)
# ef = SentenceTransformer("multi-qa-mpnet-base-dot-v1 ")

# ef = model.DefaultEmbeddingFunction()

with open("data", "r", encoding='utf-8') as file:
    text = file.read()
text_data = text.split(sep="\n")
print("length of text_data is ", len(text_data))
for data_item in text_data:
    print("data_item is: ", data_item)

text_embeddings = ef.encode(text_data)

embeddings_list = []
for embedding in text_embeddings:
    temp = embedding.tolist()
    embeddings_list.append([num * 100 for num in temp])

with open("D:/Download/OB_text_embeddings.json", "w", encoding="utf-8") as file:
    json.dump(embeddings_list, file)
