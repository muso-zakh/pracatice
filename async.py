from time import time
import aiohttp
import asyncio
import os

begin = time()
img_url = "https://picsum.photos/1000/1000"
os.makedirs('images', exist_ok=True)


async def download(session, filename):
    try:
        async with session.get(img_url) as response:
            if response.status == 200:
                response = await response.read()
                with open(filename, "wb") as img:
                    img.write(response)
                print(f"{filename} successfully downloaded!")
            else:
                print(f"Error on file {filename}: {response.status}")
    except Exception as e:
        print(f"Error on file {filename}: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 1001):
            tasks.append(
                download(session, f"images/image_{i}.jpg")
            )
        await asyncio.gather(*tasks)

asyncio.run(main())

finish = time()

print(finish - begin)
# 5.919241666793823
# 6.050390720367432
# 24.89435839653015 (1000)
