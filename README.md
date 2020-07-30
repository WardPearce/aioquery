[![GitHub issues](https://img.shields.io/github/issues/WardPearce/aioquery)](https://github.com/WardPearce/aioquery/issues)
[![GitHub license](https://img.shields.io/github/license/WardPearce/aioquery)](https://github.com/WardPearce/aioquery/blob/master/LICENSE)
[![Actions Status](https://github.com/WardPearce/aioquery/workflows/Python%20application/badge.svg)](https://github.com/WardPearce/aioquery/actions)


## Install
- Pypi: ``pip3 install aioquery``
- Git: ``pip3 install git+https://github.com/WardPearce/aioquery.git``

## API
```python
import aioquery
import asyncio


server = aioquery.client("216.52.148.47")


async def test():
    details = await server.info()
    print(
        details.protocol,
        details.hostname,
        details.map,
        details.game_dir,
        details.game_desc,
        details.app_id,
        details.players,
        details.max_players,
        details.bots,
        details.password,
        details.secure,
        details.version,
        details.game_port,
        details.steamid,
        details.spec_port,
        details.spec_name,
        details.tags,
        sep="\n"
    )

    # tags may be None instead of a list.

    if details.dedicated.dedicated:
        print("Dedicated")
    elif details.dedicated.listen:
        print("Listen")
    else:
        print("Source Tv")

    if details.os.windows:
        print("Windows")
    elif details.os.linux:
        print("Linux")
    else:
        print("Mac")

    async for player in server.players():
        print(
            player.name,
            player.id,
            player.frags,
            player.time,
            sep="\n"
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
```