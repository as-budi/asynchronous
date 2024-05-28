import asyncio
import time
import requests
import aiohttp

async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/request/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://github.com']
    
    start = time.time()
    sync_text_response = []
    for url in urls:
        sync_text_response.append(requests.get(url).text)
    end_time = time.time()
    print('Request took:', end_time - start)

    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))
    async_text_response = await asyncio.gather(*tasks)
    end_time = time.time()
    print('Async request took:', end_time - start)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())