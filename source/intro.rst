Intro
=====

Aioquery was originally created for my SourceQueryBot Discord bot.
After seeing the lack of any awaiting A2S wrappers I decided to package it.


Getting server details
----------------------

.. code-block:: python

    from aioquery import Server
    from asyncio import get_event_loop


    server = Server(
        ip="185.107.96.107",
        port=27015,
        timeout=3
    )

    async def async_loop():
        details = await server.info()

        print(details.hostname)


    get_event_loop().run_until_complete(async_loop())


Getting players
---------------

.. code-block:: python

    from aioquery import Server
    from asyncio import get_event_loop


    server = Server(
        ip="185.107.96.107",
        port=27015,
        timeout=3
    )

    async def async_loop():
        async for player in server.players():
            print(
                player.id,
                player.name,
                player.frags,
                player.time,
                sep="\n"
            )

    get_event_loop().run_until_complete(async_loop())
