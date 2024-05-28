import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    await asyncio.sleep(2)
    print("After sleep", n)

async def async_hello():
    print('Hello')

async def main():
    await asyncio.gather(async_sleep(1), async_sleep(2), async_hello())

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    elapsed = time.time() - s
    print(f"Program executed in {elapsed:0.2f} seconds.")
