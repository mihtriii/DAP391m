from loader import load_pdf
from chunker import chunk_text
from embedder import embed_text

import faiss
import numpy as np
import pickle

text = load_pdf("data/1904.08779v3.pdf")

chunks = chunk_text(text)

embeddings = []

for chunk in chunks:
    embeddings.append(embed_text(chunk))

dimension = len(embeddings[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))

faiss.write_index(index, "vector.index")

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Vector DB created")