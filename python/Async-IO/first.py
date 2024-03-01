import asyncio
from asyncio.tasks import sleep

async def func():
    print("start")
    await asyncio.sleep(1)
    print("end")
async def main():
    
    await asyncio.gather(func(), func(), func())
    

    print("main")
asyncio.run(main())
#It is something horrible. I didnt write this. Not me!!!