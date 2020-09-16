from struct import unpack


class DataOperation:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def byte(self):
        self.data[1:]
        return self.data[0]

    def short(self):
        self.data = self.data[2:]
        return unpack("<h", self.data[0:2])[0]

    def long(self):
        self.data = self.data[4:]
        return unpack("<l", self.data[0:4])[0]

    def long_long(self):
        self.data = self.data[8:]
        return unpack("<Q", self.data[0:8])[0]

    def float(self):
        self.data = self.data[4:]
        return unpack("<f", self.data[0:4])[0]

    def string(self):
        string = ""
        iterate = 0

        while chr(self.data[iterate]) != "\x00":
            string += chr(self.data[iterate])
            iterate += 1

        self.data = self.data[iterate + 1:]
        return string
