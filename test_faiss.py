import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import fitz

# Load model
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!")

# Read PDF
doc = fitz.open("test.pdf")
full_text = ""
for page_num in range(len(doc)):
    full_text += doc[page_num].get_text()

# Chunk it
def split_into_chunks(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

chunks = split_into_chunks(full_text)
print(f"Total chunks: {len(chunks)}")

# Embed all chunks
print("Embedding chunks...")
embeddings = model.encode(chunks)

# Convert to float32 (FAISS requires this)
embeddings = np.array(embeddings).astype('float32')

# Build FAISS index
print("Building FAISS index...")
dimension = embeddings.shape[1]  # 384
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
print(f"FAISS index built! Total vectors stored: {index.ntotal}")

# Now search with a question
question = "What is the CGPA?"
print(f"\nSearching for: '{question}'")

# Embed the question
question_embedding = model.encode([question])
question_embedding = np.array(question_embedding).astype('float32')

# Search top 2 most relevant chunks
distances, indices = index.search(question_embedding, k=2)

print("\nTop 2 most relevant chunks:")
for i, idx in enumerate(indices[0]):
    print(f"\n--- Result {i+1} (distance: {distances[0][i]:.4f}) ---")
    print(chunks[idx][:300])