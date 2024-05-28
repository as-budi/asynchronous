import asyncio
import time

async def async_sleep():
    print("Before sleep")
    await asyncio.sleep(5)
    print("After sleep")

async def hello():
    return 'Hello'

async def main():
    await async_sleep()
    result = await hello()
    print(result)

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    elapsed = time.time() - s
    print(f"Program executed in {elapsed:0.2f} seconds.")
