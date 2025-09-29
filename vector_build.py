from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
text = "벡터값 만들기"
embedding = model.encode(text)

print(len(embedding))   # 384
print(embedding[:10])   # 일부 값 출력
