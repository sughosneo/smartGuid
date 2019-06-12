from SmartGuid import SmartGuid
import asyncio
import unsync
async def generateGuid():

    smartGuid = SmartGuid.instance()
    return smartGuid.getGuid("a","b")

def main():

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(generateGuid())

    print(result)

if __name__ == '__main__':

    while True:

        main()
