#Jason French 5.30.23
from PyPDF2 import PdfReader

def pdf_to_text(path):
    
    text = []

    #read pdf
    pdf_file = open(path, "rb")
    pdf_reader = PdfReader(pdf_file)
    num_pages = pdf_reader.pages

    #write pdf contents to txt file
    extracted_text = open("extracted_text.txt", "w", encoding="utf-8")
    for page in num_pages:
        extracted_text.write(page.extract_text())
    extracted_text.close()

    #extract words from pdf file into list
    extracted_text = open("extracted_text.txt", "r", encoding="utf-8")
    for line in extracted_text:
        for word in list(line.split(" ")):
            text.append(word)
    extracted_text.close()

    return text

path = input("enter file path: ").replace("\"", "")

print(pdf_to_text(path))