import aioquery
import asyncio


source = aioquery.client("216.52.148.47")


async def test():
    print((await source.info()).hostname)

    async for player in source.players():
        print(player.name)


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
