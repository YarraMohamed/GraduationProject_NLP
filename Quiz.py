from Helpers.splitParaghraph import divide_text_into_paragraphs
from Helpers.extractText import extract_text_from_pdf
from Helpers.generateQuiz import generate_quiz


pdf_path = "C://Users//Lenovo//Downloads//Science-15-17.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
paragraphs = divide_text_into_paragraphs(pdf_text)

data = generate_quiz(paragraphs)

questions = data[0]
answers = data[1]
choices = data[2]

print(questions)
print(answers)
print(choices)

