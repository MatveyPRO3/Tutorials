import asyncio
import time

async def count1():
    print("One 1")
    await asyncio.sleep(0.5)
    print("Two 1")

async def count2():
    print("One 2")
    await asyncio.sleep(0.3)
    print("Two 2")
    
async def count3():
    print("One 3")
    await asyncio.sleep(1)
    print("Two 3")

async def main():
    # await asyncio.gather(count1(), count2(), count3())

    # or

    task1 = asyncio.create_task(count1())
    asyncio.create_task(count2())
    asyncio.create_task(count3())
    await task1
        
if __name__ == "__main__":

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")



