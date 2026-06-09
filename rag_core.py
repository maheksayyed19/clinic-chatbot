import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

CHROMA_DIR = "chroma_db"

SYSTEM_PROMPT = """You are a helpful patient assistant for Sunshine Clinic, Pune.
You answer questions ONLY based on the clinic information provided below.
You answer in the same language the user asks — Hindi or English.
If the user asks in Hindi, reply in Hindi. If in English, reply in English.

Rules:
- NEVER make up information not in the context
- If you don't know something, say "I don't have that information. Please call 020-25001234"
- Keep answers short and friendly — 2 to 4 lines max
- For emergencies, always mention: 9876500000

Context:
{context}

Question: {input}

Answer:"""

_qa_chain = None

def get_qa_chain():
    global _qa_chain
    if _qa_chain is not None:
        return _qa_chain

    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    print("Loading vector store...")
    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    print("Loading Groq LLM...")
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=300,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    _qa_chain = create_retrieval_chain(retriever, combine_docs_chain)

    print("RAG chain ready.")
    return _qa_chain


def ask(question: str) -> str:
    try:
        print("Question:", question)

        chain = get_qa_chain()

        result = chain.invoke({"input": question})

        print("RESULT TYPE:", type(result))
        print("RESULT:", result)

        return result["answer"].strip()

    except Exception as e:
        print("ERROR:", str(e))
        return f"Sorry, error: {str(e)}"