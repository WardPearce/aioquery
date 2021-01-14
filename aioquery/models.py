from .decorators import string_encoding


class PlayerModel:
    """Holds details on players.

    Attributes
    ----------
    id: int
        ID of user on the server, not a steam ID.
    name: str
    frags: int
    time: float
    """

    @string_encoding(["name"])
    def __init__(self, id: int, name: str, frags: int, time: float) -> None:
        self.id = id
        self.name = name
        self.frags = frags
        self.time = time


class OSModel:
    """Holds details on OS

    Attributes
    ----------
    windows: bool
    linux: bool
    mac: bool
    """

    windows = False
    linux = False
    mac = False

    def __init__(self, os_code: str) -> None:
        if os_code == "w":
            self.windows = True
        elif os_code in ("m", "o"):
            self.mac = True
        else:
            self.linux = True


class DedicatedModel:
    """Holds details on dedicated

    Attributes
    ----------
    dedicated: bool
    listen: bool
    source_tv: bool
    """

    dedicated = False
    listen = False
    source_tv = False

    def __init__(self, dedicated_code: str) -> None:
        if dedicated_code == "d":
            self.dedicated = True
        elif dedicated_code == "1":
            self.listen = True
        else:
            self.source_tv = True


class ServerModel:
    """Holds details on server.

    Attributes
    ----------
    protocol: bytes
    hostname: str
    map: str
    game_dir: str
    game_desc: str
    app_id: int
    players: int
    max_players: int
    bots: int
    dedicated: DedicatedModel
    os: OSModel
    password: str
    secure: bool
    version: str
    game_port: int
        By default None
    steamid: int
        By default None
    spec_port: int
        By default None
    spec_name: str
        By default None
    tags: list
        By default None
    gameid: int
        By default None
    """

    @string_encoding(["hostname", "spec_name", "tags", "game_desc",
                      "game_dir"])
    def __init__(self, protocol: bytes, hostname: str, map: str,
                 game_dir: str, game_desc: str, app_id: int,
                 players: int, max_players: int, bots: int,
                 dedicated: str, os: str, password: str,
                 secure: int, version: str, game_port: int = None,
                 steamid: int = None, spec_port: int = None,
                 spec_name: str = None, tags: str = None,
                 gameid: int = None) -> None:
        self.protocol = protocol
        self.hostname = hostname
        self.map = map
        self.game_dir = game_dir
        self.game_desc = game_desc
        self.app_id = app_id
        self.players = players
        self.max_players = max_players
        self.bots = bots
        self.dedicated = DedicatedModel(dedicated)
        self.os = OSModel(os)
        self.password = password
        self.secure = bool(secure)
        self.version = version
        self.game_port = game_port
        self.steamid = steamid
        self.spec_port = spec_port
        self.spec_name = spec_name
        self.tags = tags.split(",") if tags else None
        self.gameid = gameid
