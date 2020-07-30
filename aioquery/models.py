class PlayerModel:
    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.frags = data["frags"]
        self.time = data["time"]


class OSModel:
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
    def __init__(self, data: dict) -> None:
        self.protocol = data["protocol"]
        self.hostname = data["hostname"]
        self.map = data["map"]
        self.game_dir = data["game_dir"]
        self.game_desc = data["game_desc"]
        self.app_id = data["app_id"]
        self.players = data["players"]
        self.max_players = data["max_players"]
        self.bots = data["bots"]
        self.dedicated = DedicatedModel(data["dedicated"])
        self.os = OSModel(data["os"])
        self.password = data["password"]
        self.secure = bool(data["secure"])
        self.version = data["version"]

        self.game_port = data["game_port"] if "game_port" in data else None
        self.steamid = data["steamid"] if "steamid" in data else None
        self.spec_port = data["spec_port"] if "spec_port" in data else None
        self.spec_name = data["spec_name"] if "spec_name" in data else None
        self.tags = data["tags"].split(",") if "tags" in data and \
            "," in data else None
