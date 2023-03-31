# encoding:utf-8
class ReadFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ReadFile(README.md) as fread:
    f.write("Learning context manager")
    f.write("Writing into file")