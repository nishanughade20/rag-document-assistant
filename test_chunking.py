import streamlit as st
import fitz

# ---- Chunking function ----
def split_into_chunks(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# ---- Page config ----
st.set_page_config(page_title="RAG Document Assistant", page_icon="📄")
st.title("📄 RAG Document Assistant")
st.write("Upload any document and ask questions about it!")
st.divider()

# ---- Step 1: Upload ----
st.subheader("Step 1 — Upload your document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully: " + uploaded_file.name)

    # Extract text
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        full_text += page.get_text()

    # Chunk the text
    chunks = split_into_chunks(full_text)

    # Show stats
    st.info(f"📊 Pages: {len(doc)} | Characters: {len(full_text)} | Chunks created: {len(chunks)}")

    # Show chunks
    with st.expander("👀 See all chunks"):
        for i, chunk in enumerate(chunks):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(chunk)
            st.divider()

st.divider()

# ---- Step 2: Question ----
st.subheader("Step 2 — Ask a question")
user_question = st.text_input("Type your question here...")

if st.button("Get Answer"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a document first!")
    elif user_question == "":
        st.warning("⚠️ Please type a question!")
    else:
        st.info("🤖 Answer will appear here soon. We're building this next!")