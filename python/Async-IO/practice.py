import asyncio
import requests
from time import sleep

async def counter():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.25)
        # sleep(0.25)
        

async def requester():
    status_code = requests.get("http://google.com")
    print(status_code)
    await asyncio.sleep(1)
    status_code = requests.get("http://dji.com")
    print(status_code)
    
async def main():
    task = asyncio.create_task(counter())
    await requester()
    print("requests made")
    await task

if __name__ == "__main__":
    asyncio.run(main())

#https://www.youtube.com/watch?v=nFn4_nA_yk8