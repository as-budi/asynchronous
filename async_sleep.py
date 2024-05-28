import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    await asyncio.sleep(5)
    print("After sleep", n)

async def async_hello():
    print('Hello')

async def main():
    await async_sleep(1)
    await async_sleep(2)
    await async_hello()

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    elapsed = time.time() - s
    print(f"Program executed in {elapsed:0.2f} seconds.")
