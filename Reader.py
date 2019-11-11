import sys
from TIGr import AbstractSourceReader


# This needs to be updated (maybe with a Design Pattern)
# Detects if data is inside standard in (which means it has been piped to the program) and caches that
# if there is no stdin then try to read from a file location
# else read the cache at last resort
class Reader(AbstractSourceReader):
    def go(self):
        content = []
        # When data is given by piping
        if not sys.stdin.isatty():
            data = sys.stdin.readlines()
            if len(data) > 0:
                f = open("cache.txt", "w")
                for line in data:
                    content.append(line.strip().split(' '))
                    f.write(line)
                f.close()
        else:
            with open(sys.argv[1], "r") as f:
                for line in f.readlines():
                    content.append(line.strip().split(' '))
        if not content:
            with open("cache.txt", "r") as f:
                for line in f.readlines():
                    content.append(line.strip().split(' '))
        self.parser.parse(content)