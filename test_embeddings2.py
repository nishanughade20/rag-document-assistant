from sentence_transformers import SentenceTransformer
import fitz

# Load model
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!")

# Read your PDF
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
print(f"Done! Embeddings shape: {embeddings.shape}")
print(f"This means {embeddings.shape[0]} chunks, each represented by {embeddings.shape[1]} numbers")