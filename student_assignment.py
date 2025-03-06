from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
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


def hw02_2(q2_pdf):
    pass


def main():
    hw02_1(q1_pdf)


if __name__ == '__main__':
    main()
