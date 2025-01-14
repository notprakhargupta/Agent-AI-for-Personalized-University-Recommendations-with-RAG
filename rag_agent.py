
import openai
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Initialize the vector database
def load_vector_database():
    return FAISS.load_local("faiss_index", OpenAIEmbeddings())

# Retrieval-Augmented Generation (RAG) pipeline
def rag_pipeline(query):
    vector_db = load_vector_database()
    docs = vector_db.similarity_search(query, k=5)
    
    # Format retrieved docs
    context = "\n".join([doc.page_content for doc in docs])

    # GPT-4 query with context
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Given the following university and scholarship data:\n{context}\nAnswer the query: {query}",
        max_tokens=500
    )
    
    return response['choices'][0]['text'].strip()
