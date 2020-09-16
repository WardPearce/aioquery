import asynctest

from .. import AioQuery
from ..models import ServerModel, PlayerModel
from ..exceptions import UnableToConnect, DidNotReceive


class AioQueryTest(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self):
        test_servers = [
            "216.52.148.47",
            "92.119.148.18",
            "74.91.119.188",
            "74.91.113.83",
            "104.153.105.44",
            "92.119.148.200"
        ]

        self.client = None

        for server in test_servers:
            try:
                self.client = AioQuery(server)
            except (UnableToConnect, DidNotReceive):
                pass
            else:
                break

    async def test_server(self):
        self.assertIsNot(self.client, None)

        info = await self.client.info()

        self.assertTrue(type(info) == ServerModel)

    async def test_players(self):
        async for player in self.client.players():
            self.assertTrue(
                type(player) == PlayerModel
            )

    async def test_errors(self):
        with self.assertRaises((DidNotReceive, UnableToConnect)):
            await AioQuery("").info()
