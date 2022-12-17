import asyncio

import aiohttp

async def download_page(session, url):

    async with session.get(url) as response:

        return await response.text()

async def main():

    async with aiohttp.ClientSession() as session:

        html = await download_page(session, 'http://example.com')

        print(html)

loop = asyncio.get_event_loop()

loop.run_until_complete(main())
