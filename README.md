## Install
- Pypi: ``pip3 install aioquery``
- Git: ``pip3 install git+https://github.com/WardPearce/aioquery.git``

## API
- aioquery.client(ip, port=27015, timeout=3)
    - info(self)
    - challenge(self)
    - players(self)

### Example
```py
import asyncio
import aioquery

async def testing():
    query = aioquery.client("216.52.148.47", 27015)

    server_info = await query.info()
    players = await query.players()

    print(server_info)
    print(players)

loop = asyncio.get_event_loop()
loop.run_until_complete(testing())
```