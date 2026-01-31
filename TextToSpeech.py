import PyPDF2
import pyttsx3
import time

pdf_path = "princeony.pdf"

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 160)

with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    print(f"Total Pages Found: {len(reader.pages)}")

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text and text.strip():
            print(f"Reading page {i+1}...")

            engine.say(text)
            engine.runAndWait()   # 🔑 MUST be here
            time.sleep(0.3)
