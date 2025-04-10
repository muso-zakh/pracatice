import time
from pdf2image import convert_from_path
import os 
import asyncio
import fitz

poppler_path ="C:\\Users\\user\\Documents\\poppler-24.08.0\\Library\\bin"
pdf_pap = "C:\\Users\\user\\Documents\\pdfs"
saving_folder = "C:\\Users\\user\\Documents\\images"

start = time.time()

async def converted(pdf_path):
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    os.makedirs(saving_folder, exist_ok=True)
    c = 1

    for page in pages:
        img_name=f"img-{c}.jpeg"
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        c += 1

async def main():
    files = os.listdir(pdf_pap)
    tasks = []

    for file in files:
        # pdf_path = f"C:\\Users\\user\\Documents\\pdfs\\{files[i]}"
        pdf_path = os.path.join(pdf_pap, file)

        tasks.append(converted(pdf_path))
    
    await asyncio.gather(*tasks)

asyncio.run(main())
end = time.time()
print(end-start)