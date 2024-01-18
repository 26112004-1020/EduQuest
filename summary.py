import os
import PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

pdf_file_path = r"D:\ML procts\Hack IT SSN\End-to-End Platform for Students and Universities.pdf"

pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

pdf_text = ""
for page_num in range(len(pdf_reader.pages)):
    page_text = pdf_reader.pages[page_num].extract_text().lower()
    pdf_text += page_text.replace('\n', ' ') 

pdf_file.close()

chunk_size = 1024

for i in range(0, len(pdf_text), chunk_size):
    chunk = pdf_text[i:i + chunk_size]
    
    response = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
    
    print(f"Summary for Chunk {i//chunk_size + 1}:\n{response[0]['summary_text']}\n")
