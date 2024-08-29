#!/usr/bin/env python3


import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)
async def main():

    context = await Context.create_client_context()

    await asyncio.sleep(2)
    with open('data.csv', 'r') as file:
        for line in file:
            payload = line.encode('utf-8')
            request = Message(code=PUT, payload=payload, uri="coap://192.168.100.102/news")
            response = await context.request(request).response
            print("Result: %s\n%r" % (response.code, response.payload))
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
