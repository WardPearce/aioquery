import typing

from asyncio_dgram import connect
from asyncio import wait_for

from .models import PlayerModel, ServerModel
from .data_operations import DataOperation
from .exceptions import UnableToConnect, DidNotReceive, InvalidServer


__version__ = "1.0.0"


class client:
    _challenge = None

    S2A_INFO_SOURCE = chr(0x49)

    A2S_PLAYERS = b"\xFF\xFF\xFF\xFF\x55"
    A2S_INFO = b"\xFF\xFF\xFF\xFFTSource Engine Query\x00"

    def __init__(self, ip: str, port: int = 27015, timeout: int = 3):
        """
        Handles interactions with a source server.

        Paramters
        ---------
        ip: str
            Server IP address.
        port: int
            Port of server, defaults to 27015.
        timeout: int
            How long to wait for the server, defaults to 3 seconds.
        """

        self.ip = ip
        self.port = port
        self.timeout = timeout

    async def _send_recv(self, package: bytes) -> bytes:
        """
        Sends and recives data.

        Paramters
        ---------
        package: bytes
            Package to send

        Returns
        -------
        bytes

        Raises
        ------
        UnableToConnect
            Raised when connection fails
        DidNotReceive
            Raised when didn't receive data within timeout.
        """

        try:
            stream = await connect((self.ip, self.port))
        except Exception:
            raise UnableToConnect()
        else:
            await stream.send(package)

            try:
                data = await wait_for(stream.recv(), self.timeout)

                stream.close()
            except Exception:
                raise DidNotReceive()
            else:
                return data[0]

    async def info(self) -> ServerModel:
        """
        Returns details around A2S server.

        Returns
        -------
        ServerModel
            Holds data around server.
        """

        data = await self._send_recv(self.A2S_INFO)

        data = data[4:]
        header, data = DataOperation(data).byte()

        if chr(header) == self.S2A_INFO_SOURCE:
            result = {}

            result["protocol"], data = DataOperation(data).byte()
            result["hostname"], data = DataOperation(data).string()
            result["map"], data = DataOperation(data).string()
            result["game_dir"], data = DataOperation(data).string()
            result["game_desc"], data = DataOperation(data).string()
            result["app_id"], data = DataOperation(data).short()
            result["players"], data = DataOperation(data).byte()
            result["max_players"], data = DataOperation(data).byte()
            result["bots"], data = DataOperation(data).byte()

            dedicated, data = DataOperation(data).byte()
            result["dedicated"] = chr(dedicated)

            os, data = DataOperation(data).byte()
            result["os"] = chr(os)

            result["password"], data = DataOperation(data).byte()
            result["secure"], data = DataOperation(data).byte()
            result["version"], data = DataOperation(data).string()

            edf, data = DataOperation(data).byte()

            try:
                if edf & 0x80:
                    result["game_port"], data = DataOperation(data).short()
                if edf & 0x10:
                    result["steamid"], data = DataOperation(data).long_long()
                if edf & 0x40:
                    result["spec_port"], data = DataOperation(data).short()
                    result["spec_name"], data = DataOperation(data).string()
                if edf & 0x10:
                    result["tags"], data = DataOperation(data).string()
            except Exception:
                pass

            return ServerModel(result)
        else:
            raise InvalidServer()

    async def challenge(self) -> bytes:
        """ Get challenge number for A2S_PLAYER query. """

        data = await self._send_recv(self.A2S_PLAYERS + b"0xFFFFFFFF")
        self._challenge = data[5:]

        return self._challenge

    async def players(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Yields players on server.

        Yields
        ------
        PlayerModel
            Holds player data.
        """

        if self._challenge is None:
            await self.challenge()

        data = await self._send_recv(self.A2S_PLAYERS + self._challenge)
        data = data[4:]

        _, data = DataOperation(data).byte()
        num, data = DataOperation(data).byte()

        for index in range(num):
            _, data = DataOperation(data).byte()

            player = {}
            player["id"] = index + 1
            player["name"], data = DataOperation(data).string()
            player["frags"], data = DataOperation(data).long()
            player["time"], data = DataOperation(data).float()

            yield PlayerModel(player)
