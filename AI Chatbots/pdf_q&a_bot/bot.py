import os
import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 🔐 Your Hugging Face API Key
HUGGINGFACE_API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# 📄 Load PDFs
def load_pdfs(folder_path):
    all_docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            all_docs.extend(loader.load())
    return all_docs

# ✂️ Chunk PDFs
def chunk_docs(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)

# 💾 Store in Chroma
def store_chunks(chunks, persist_dir="chroma_db"):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb

# 🧠 Answer from context via HF API
def ask_question(vectordb, query):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"Answer the question based on the context below.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.5,
        }
    }

    print("\n📡 Sending request to HuggingFace API...")
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        output = response.json()
        print("\n✅ Answer:\n")
        print(output[0]["generated_text"].replace(prompt, "").strip())
    else:
        print(f"❌ API Error {response.status_code}: {response.text}")

# 🧪 Run Everything
if __name__ == "__main__":
    folder = "AI_learning_Short_term\week_02_mini_AI_projects\day_05_pdf_Q&A_bot\pdf_qna_bot\project"

    print("🔍 Loading PDFs...")
    docs = load_pdfs(folder)
    if not docs:
        raise ValueError("❌ No PDFs found!")

    print(f"✅ Loaded {len(docs)} pages.")

    print("✂️ Splitting into chunks...")
    chunks = chunk_docs(docs)
    print(f"✅ Chunked into {len(chunks)} segments.")

    print("💾 Storing in vector DB...")
    vectordb = store_chunks(chunks)
    print("✅ DB ready.")

    print("🤖 Ask me anything about the PDFs!")
    while True:
        question = input("\n❓ Ask a question (type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        ask_question(vectordb, question)
