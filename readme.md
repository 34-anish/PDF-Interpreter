Getting the GUI
```
import streamlit as st

# def main():
st.set_page_config(page_title = "Chat with pdf" ,page_icon =":books:")
st.header("Chat with multiple PDFs :books:")
st.text_input ("Ask a question about the documents")
with st.sidebar:
    st.subheader("The documents")
    st.file_uploader("Upload your pdf here")
    st.button("process")
	
```
![dcb04cdc8145139a75593f855a006fa8.png](../_resources/dcb04cdc8145139a75593f855a006fa8.png)
![e33cb8ad2dba0d2654491300b813a968.png](../_resources/e33cb8ad2dba0d2654491300b813a968.png)
**Explanation**
- The pdfs can be entered by the users , the pdf is divided into the chunk of text which is converted into the embeddings(which is nothing but a number or a vector/number representation of the text)
- The embeddings are stored in the database (chroma, pinecone)
- The questions asked by the users are stored in the database
- The *semantic search* is done which means to find the similarity with the questions and the embeddings
*Accepting the multiple pdfs to read over*
The next step will be to accept the multiple pdfs and convert it into the texts
![88945e0425320c78808af4002dca1e6f.png](../_resources/88945e0425320c78808af4002dca1e6f.png) 
```
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(pdf_reader)
    return text

st.set_page_config(page_title = "Chat with pdf" ,page_icon =":books:")
st.header("Chat with multiple PDFs :books:")
st.text_input ("Ask a question about the documents")
with st.sidebar:
    st.subheader("The documents")
    pdf_docs = st.file_uploader("Upload your pdf here",accept_multiple_files= True)
    if st.button("process"):
        with st.spinner("Processing"):
            raw_text = get_pdf_text(pdf_docs)
st.write(raw_text)

```
![22eb4e502b71aa3c35aa1ed293f1434b.png](../_resources/22eb4e502b71aa3c35aa1ed293f1434b.png)
Next up we need to deal with getting the chunks of the text from the entered text .
![6b75143a19cfa7c59f43229610a1deb8.png](../_resources/6b75143a19cfa7c59f43229610a1deb8.png)
![9e96a1f532c2c64bdf86c386c64fd965.png](../_resources/9e96a1f532c2c64bdf86c386c64fd965.png)
```
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(pdf_reader)
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks


st.set_page_config(page_title = "Chat with pdf" ,page_icon =":books:")
st.header("Chat with multiple PDFs :books:")
st.text_input ("Ask a question about the documents")
with st.sidebar:
    st.subheader("The documents")
    pdf_docs = st.file_uploader("Upload your pdf here",accept_multiple_files= True)
    if st.button("process"):
        with st.spinner("Processing"):

            # Getting the raw text
            raw_text = get_pdf_text(pdf_docs)

            #Getting the chunks of the text
            text_chunks = get_text_chunks(raw_text)
            st.write(text_chunks)
        # st.write(raw_text)
```
![67dc9bac4ce6f563ba2dccd7e5eb019d.png](../_resources/67dc9bac4ce6f563ba2dccd7e5eb019d.png)
example 1 and 2 are two chinks of size 1000 and 200 overlapping meaning the first word of the 2nd chunk starts 200 words before of the 2nd chunk.
![3bab14639ac6bcfd1287b403267857de.png](../_resources/3bab14639ac6bcfd1287b403267857de.png)
Embeddings are stored locally into the vector store with the help of 	FAISS  
![f59861667f237a54d3886fe8a6fda21e.png](../_resources/f59861667f237a54d3886fe8a6fda21e.png)
![a55932b3b18be6fd0ebcc39da03d3910.png](../_resources/a55932b3b18be6fd0ebcc39da03d3910.png)
```
import streamlit as st
from dotenv import load_dotenv
from secret_key import openapi_key
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(pdf_reader)
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks , embedding=embeddings)
    return vectorstore

os.environ["OPENAI_API_KEY"] = openapi_key
st.set_page_config(page_title = "Chat with pdf" ,page_icon =":books:")
st.header("Chat with multiple PDFs :books:")
st.text_input ("Ask a question about the documents")
with st.sidebar:
    st.subheader("The documents")
    pdf_docs = st.file_uploader("Upload your pdf here",accept_multiple_files= True)
    if st.button("process"):
        with st.spinner("Processing"):

            # Getting the raw text
            raw_text = get_pdf_text(pdf_docs)

            #Getting the chunks of the text
            text_chunks = get_text_chunks(raw_text)

            #Getting the vector store
            vectorstore = get_vectorstore(text_chunks)
            st.write(text_chunks)
        # st.write(raw_text)
```
**![b07aba2019e4cd4dcb417a54f3cbfb42.png](../_resources/b07aba2019e4cd4dcb417a54f3cbfb42.png)**
Inspired by: https://github.com/alejandro-ao/ask-multiple-pdfs