import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    n = max(2, n)
    for i in range(1, n):
        yield i
        await asyncio.sleep(i)
    print("After sleep", n)

async def async_hello():
    print('Hello')

async def main():
    async for k in async_sleep(5):
        print(k)

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    elapsed = time.time() - s
    print(f"Program executed in {elapsed:0.2f} seconds.")
