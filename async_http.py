import asyncio
import time
import requests

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/request/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://github.com']
    
    start = time.time()
    for url in urls:
        requests.get(url)
    end_time = time.time()
    print('Request took:', end_time - start)


if __name__ == "__main__":
    asyncio.run(main())