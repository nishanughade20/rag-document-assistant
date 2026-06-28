import fitz  # this is PyMuPDF

# Open a PDF file
doc = fitz.open("test.pdf")

# Loop through each page and extract text
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    print(f"--- Page {page_num + 1} ---")
    print(text)