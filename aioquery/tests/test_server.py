import asynctest

from .. import Server
from ..models import ServerModel, PlayerModel
from ..exceptions import UnableToConnect, DidNotReceive


class AioQueryTest(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self):
        test_servers = [
            "185.107.96.107",
            "92.119.148.18",
            "74.91.119.188",
            "74.91.113.83",
            "104.153.105.44",
            "92.119.148.200"
        ]

        self.client = None

        for server in test_servers:
            try:
                self.client = Server(server)
            except (UnableToConnect, DidNotReceive):
                pass
            else:
                break

    async def test_server(self):
        self.assertIsNot(self.client, None)

        info = await self.client.info()

        self.assertTrue(type(info) == ServerModel)

    async def test_players(self):
        self.assertIsNot(self.client, None)

        async for player in self.client.players():
            self.assertTrue(
                type(player) == PlayerModel
            )

    async def test_errors(self):
        with self.assertRaises((DidNotReceive, UnableToConnect)):
            await Server("").info()
