
import os
import fitz
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    try:

        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        if len(text.strip()) < 50:  
            raise ValueError("Text too short. Using OCR fallback.")
        return text
    except Exception as e:
        print(f"Fallback to OCR for {pdf_path} due to: {e}")
        return extract_text_with_ocr(pdf_path)



def extract_text_with_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    ocr_text = ""
    for image in images:
        ocr_text += pytesseract.image_to_string(image)
    return ocr_text


def ocr_pdf(pdf_path):
    text = ''
    try:
        images = convert_from_path(pdf_path)
        for i, img in enumerate(images):
            text += pytesseract.image_to_string(img)
    except Exception as e:
        print(f"OCR failed for {pdf_path}: {e}")
    return text

def process_all_pdfs(pdf_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file)
            text = extract_text_from_pdf(pdf_path)
            out_path = os.path.join(output_dir, file.replace(".pdf", ".txt"))
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Processed: {file}")



if __name__ == "__main__":
    process_all_pdfs("backend/data/arxiv_papers", "backend/data/arxiv_texts")
