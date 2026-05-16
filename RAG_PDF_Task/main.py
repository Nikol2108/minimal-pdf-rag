import os
import argparse
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

PDF_PATH = "data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf"
INDEX_PATH = "faiss_index"
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 4


def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()


def split_text_into_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(documents)


def create_embeddings_and_save_to_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(INDEX_PATH)
    return vector_store


def load_or_build_vector_store(pdf_path: str):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(
            INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )

    documents = load_pdf(pdf_path)
    chunks = split_text_into_chunks(documents)
    return create_embeddings_and_save_to_vector_store(chunks)


def user_question_get_relevant_chunks(vector_store, question: str, k: int = TOP_K):
    return vector_store.similarity_search(question, k=k)


def answer_question_with_context(question: str, source_chunks):
    context = "\n\n".join(chunk.page_content for chunk in source_chunks)

    prompt = ChatPromptTemplate.from_template(
        """You are a careful assistant.
Answer the question using only the context below.
If the answer is not in the context, say exactly:
I could not find the answer in the document.

Context:
{context}

Question:
{question}

Answer:"""
    )

    llm = ChatOpenAI(model=LLM_MODEL, temperature=0)
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": question})
    return response.content.strip()


def return_answer_alongside_sources(answer: str, source_chunks):
    print("\nAnswer:\n")
    print(answer)
    print("\nSource Chunks:\n")

    for i, chunk in enumerate(source_chunks, start=1):
        page = chunk.metadata.get("page", "Unknown")
        source = chunk.metadata.get("source", "Unknown")
        text = chunk.page_content.strip().replace("\n", " ")
        print(f"--- Source {i} | page {page} | {source} ---")
        print(text[:800])
        print()


def validate_environment(pdf_path: str):
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")


def main():
    parser = argparse.ArgumentParser(description="Minimal PDF RAG app")
    parser.add_argument("--pdf", default=PDF_PATH, help="Path to the PDF file")
    args = parser.parse_args()

    validate_environment(args.pdf)

    vector_store = load_or_build_vector_store(args.pdf)

    print("\nPDF RAG Assistant is ready.")
    print("Type your question and press Enter.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("Ask a question: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        source_chunks = user_question_get_relevant_chunks(vector_store, question)
        answer = answer_question_with_context(question, source_chunks)
        return_answer_alongside_sources(answer, source_chunks)



if __name__ == "__main__":
    main()