import csv
import requests
import sqlite3
import time

started_at = time.time()

def get_pdf_from_url(name: str, url: str):
    print(f"{name},,, {url}")
    # response = requests.get(url, stream=True)
    # content = response.text

    # index = content.find('href="/public/uploads/')
    # if index != -1:
    #     start_url = index + 6
    #     end_url = content.find('.pdf"') + 4
    #     pdf_url = f"https://vexillum.uz{content[start_url:end_url]}"

    #     with open(f"files_100/{name}.pdf", "wb") as file:
    #         file.write(requests.get(pdf_url).content)
    #     print(f"{name}.pdf has been downloaded")
    # else:
    #     print(f"{name} not found in url {url}")


with open("C:\\Users\\user\\Documents\\python\\5_11-dars\\standards.csv", 'r', encoding='utf-8') as f:
    reads =  f.readlines()
    for line in reads:
        row = line.split(",")
        if len(row)>2:
            row[0] = row[:-1]
        

        get_pdf_from_url(row[0], row[1])

finished_at = time.time()

print(finished_at - started_at)