import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename


def read_pdf(file_path):
    """Read PDF and convert text to speech."""
    pdf_reader = PyPDF2.PdfReader(file_path)
    pages = len(pdf_reader.pages)
    print(f"Total pages: {pages}")

    speaker = pyttsx3.init()

    for num in range(pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()
        if text:
            speaker.say(text)
            speaker.runAndWait()
        else:
            print(f"Page {num + 1} has no readable text.")


if __name__ == "__main__":
    book = askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    if book:
        read_pdf(book)
    else:
        print("No file selected.")
