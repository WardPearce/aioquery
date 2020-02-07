# TODO
# More game support
# Player time should be a object.

import asyncio
import socket
import struct
import time

A2S_INFO = b"\xFF\xFF\xFF\xFFTSource Engine Query\x00"
A2S_PLAYERS = b"\xFF\xFF\xFF\xFF\x55"

READ_BYTES = 4096

S2A_INFO_SOURCE = chr(0x49)

class source_query(object):
    __challenge = None

    def __init__(self, ip, port=27015, timeout=5.0):
        self.ip = socket.gethostbyname(ip)
        self.port = port
        self.timeout = timeout

    async def get_info(self):
        """ Retrieves information about the server including, but not limited to: its name, the map currently being played, and the number of players. """
        reader, writer = await asyncio.open_connection(self.ip, self.port)

        print(writer)

        writer.write(A2S_INFO)
        
        before = time.time()

        try:
            data = await reader.read(READ_BYTES)
        except:
            return False

        after = time.time()
        
        data = data[4:]
        header, data = self.__get_byte(data)

        result = {
            "ping": int((after - before) * 1000)
        }

        if chr(header) == S2A_INFO_SOURCE:
            result["protocol"], data = self.__get_byte(data)
            result["hostname"], data = self.__get_string(data)
            result["map"], data = self.__get_string(data)
            result["game_dir"], data = self.__get_string(data)
            result["game_desc"], data = self.__get_string(data)
            result["app_id"], data = self.__get_short(data)
            result["players"], data = self.__get_byte(data)
            result["max_players"], data = self.__get_byte(data)
            result["bots"], data = self.__get_byte(data)
            
            dedicated, data = self.__get_byte(data)
            if chr(dedicated) == "d":
                result["dedicated"] = "Dedicated"
            elif dedicated == 'l':
                result["dedicated"] = "Listen"
            else:
                result["dedicated"] = 'SourceTV'

            os, data = self.__get_byte(data)
            if chr(os) == "w":
                result["os"] = "Windows"
            elif chr(os) in ("m", "o"):
                result["os"] = "Mac"
            else:
                result["os"] = "Linux"

            result["password"], data = self.__get_byte(data)
            result["secure"], data = self.__get_byte(data)
            result["version"], data = self.__get_string(data)

            edf, data = self.__get_byte(data)

            try:
                if edf & 0x80:
                    result["game_port"], data = self.__get_short(data)
                if edf & 0x10:
                    result["steamid"], data = self.__get_long_long(data)
                if edf & 0x40:
                    result["spec_port"], data = self.__get_short(data)
                    result["spec_name"], data = self.__get_string(data)
                if edf & 0x10:
                    result["tags"], data = self.__get_string(data)
            except:
                pass

        return result

    def get_challenge(self):
        """ Get challenge number for A2S_PLAYER query. """

        self.__sock.send(A2S_PLAYERS + b"0xFFFFFFFF")
        try:
            data = self.__sock.recv(4096)
        except:
            return False

        self.__challenge = data[5:]

        return True

    def get_players(self):
        """ Retrieve information about the players currently on the server. """
        if self.__challenge is None:
            self.get_challenge()

        self.__sock.send(A2S_PLAYERS + self.__challenge)
        try:
            data = self.__sock.recv(4096)
        except:
            return False

        data = data[4:]

        header, data = self.__get_byte(data)
        num, data = self.__get_byte(data)
        result = []

        for i in range(num):
            data = self.__get_byte(data)[1]

            player = {}
            player["id"] = i + 1  # ID of All players is 0
            player["name"], data = self.__get_string(data)
            player["frags"], data = self.__get_long(data)
            player["time"], data = self.__get_float(data)

            result.append(player)

        return result

    def __get_byte(self, data):
        return data[0], data[1:]

    def __get_short(self, data):
        return struct.unpack("<h", data[0:2])[0], data[2:]

    def __get_long(self, data):
        return struct.unpack("<l", data[0:4])[0], data[4:]

    def __get_long_long(self, data):
        return struct.unpack("<Q", data[0:8])[0], data[8:]

    def __get_float(self, data):
        return struct.unpack("<f", data[0:4])[0], data[4:]

    def __get_string(self, data):
        s = ""
        i = 0
        while chr(data[i]) != "\x00":
            s += chr(data[i])
            i += 1
        return s, data[i + 1:]

if __name__ == '__main__':
    async def testing():
        query = source_query("216.52.148.47", 27015)
        res = await query.get_info()

        print(res)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())
    loop.close()