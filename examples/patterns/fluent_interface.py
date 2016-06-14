# https://en.wikipedia.org/wiki/Fluent_interface

class Poem(object):
    def __init__(self, content):
        self.content = content

    def indent(self, spaces):
        self.content = " " * spaces + self.content
        return self

    def suffix(self, content):
        self.content = self.content + " - " + content
        return self


if __name__ == "__main__":
    poem = Poem("Road Not Travelled").indent(4).suffix("Robert Frost").content
    print(poem)
