from Helpers.extractText import extract_text_from_pdf
from Helpers.generateSummary import generate_summary

pdf_path = "C://Users//Lenovo//Downloads//Science-15-17.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
summary = generate_summary(pdf_text)

print(summary)
