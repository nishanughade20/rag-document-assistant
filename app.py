import streamlit as st

# Page title
st.set_page_config(page_title="RAG Document Assistant", page_icon="📄")

# Header
st.title("📄 RAG Document Assistant")
st.write("Upload any document and ask questions about it!")

# Divider line
st.divider()

# File upload section
st.subheader("Step 1 — Upload your document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully: " + uploaded_file.name)

# Divider line
st.divider()

# Question section
st.subheader("Step 2 — Ask a question")
user_question = st.text_input("Type your question here...")

# Submit button
if st.button("Get Answer"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a document first!")
    elif user_question == "":
        st.warning("⚠️ Please type a question!")
    else:
        st.info("🤖 Answer will appear here soon. We're building this next!")
