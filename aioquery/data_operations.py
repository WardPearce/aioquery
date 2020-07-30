from struct import unpack


class DataOperation:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def byte(self):
        return self.data[0], self.data[1:]

    def short(self):
        return unpack("<h", self.data[0:2])[0], self.data[2:]

    def long(self):
        return unpack("<l", self.data[0:4])[0], self.data[4:]

    def long_long(self):
        return unpack("<Q", self.data[0:8])[0], self.data[8:]

    def float(self):
        return unpack("<f", self.data[0:4])[0], self.data[4:]

    def string(self):
        string = ""
        iterate = 0

        while chr(self.data[iterate]) != "\x00":
            string += chr(self.data[iterate])
            iterate += 1

        return string, self.data[iterate + 1:]
