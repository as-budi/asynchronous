import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    await asyncio.sleep(n)
    print("After sleep", n)

async def async_hello():
    print('Hello')

async def main():
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(7), 5), async_sleep(2), async_hello())
    except asyncio.TimeoutError:
        print('Timeout error')

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    elapsed = time.time() - s
    print(f"Program executed in {elapsed:0.2f} seconds.")
