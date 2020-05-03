## Install
- Pypi: ``pip3 install aioquery``
- Git: ``pip3 install git+https://github.com/WardPearce/aioquery.git``

## API
- aioquery(ip, port=27015, timeout=3)
    - get_info(self)
    - get_challenge(self)
    - get_players(self)

### Example
```py
import asyncio
from aioquery import aioquery

async def testing():
    query = aioquery("216.52.148.47", 27015)

    server_info = await query.get_info()
    players = await query.get_players()

    print(server_info)
    print(players)

loop = asyncio.get_event_loop()
loop.run_until_complete(testing())
loop.close()
```