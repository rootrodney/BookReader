# Import ing the pyttsx3 library for text-to-speech and PyPDF2 library for handling PDF files
import pyttsx3
import PyPDF2

# Opening a PDF file named 'RodneyCv.pdf' in binary mode ('rb')
book = open('BIRTH.pdf', 'rb')

# Creating a PdfFileReader object to read the PDF file
pdfreader = PyPDF2.PdfFileReader(book)

# Getting the total number of pages in the PDF
pages = pdfreader.numPages

# Printing the total number of pages
print(f"Total number of pages: {pages}")

# Initializing the text-to-speech engine
speaker = pyttsx3.init()

# Getting the list of available voices
voices = speaker.getProperty("voices")

# Setting the voice to the second voice in the list (you can change this index based on available voices)
speaker.setProperty("voice", voices[1].id)

# Looping through each page of the PDF
for num in range(0, pages):
    # Getting the specific page using the page number
    page = pdfreader.getPage(num)

    # Extracting text from the page
    text = page.extractText()

    # Using the text-to-speech engine to speak the extracted text
    speaker.say(text)

    # Running the text-to-speech engine to play the speech
    speaker.runAndWait()

# Closing the PDF file after reading all the pages
book.close()
