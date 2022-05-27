class File:
    def __init__(self, name='', content=None, size=0):
        self.name = name
        self.content = content
        self.size = size


class Directory:
    def __init__(self, files=None, subdirectories=None):
        self.files = files if files is not None else []
        self.subdirectories = subdirectories if subdirectories is not None else []


def getSize(dir):
    size = 0
    for file in dir.files:
        size += file.size
    for subdir in dir.subdirectories:
        size += getSize(subdir)
    return size
