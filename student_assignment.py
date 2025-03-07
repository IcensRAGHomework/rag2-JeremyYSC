from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(pdf_file):
    loader = PyPDFLoader(pdf_file)
    documents = loader.load()
    print(documents)

    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,  # 每頁內容通常不會超過1000字元
        chunk_overlap=0  # 無重疊
    )

    chunks = text_splitter.split_documents(documents)
    print(chunks[-1])
    return chunks[-1]


def hw02_2(pdf_file):
    loader = PyPDFLoader(pdf_file)
    documents = loader.load()
    full_text = "\n".join(doc.page_content for doc in documents)
    # print(full_text)

    text_splitter = CharacterTextSplitter(
        separator="[\s\n]第.+[條章][\s\n]",
        chunk_size=10,
        chunk_overlap=0,
        is_separator_regex=True
    )

    chunks = text_splitter.split_text(full_text)
    print(chunks)
    print(len(chunks))
    return len(chunks)


def main():
    # hw02_1(q1_pdf)
    hw02_2(q2_pdf)


if __name__ == '__main__':
    main()
