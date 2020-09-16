from struct import unpack


class DataOperations:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def byte(self):
        data = self.data[0]
        self.data = self.data[1:]
        return data

    def short(self):
        data = unpack("<h", self.data[0:2])[0]
        self.data = self.data[2:]
        return data

    def long(self):
        data = unpack("<l", self.data[0:4])[0]
        self.data = self.data[4:]
        return data

    def long_long(self):
        data = unpack("<Q", self.data[0:8])[0]
        self.data = self.data[8:]
        return data

    def float(self):
        data = unpack("<f", self.data[0:4])[0]
        self.data = self.data[4:]
        return data

    def string(self):
        string = ""
        iterate = 0

        while chr(self.data[iterate]) != "\x00":
            string += chr(self.data[iterate])
            iterate += 1

        self.data = self.data[iterate + 1:]
        return string
