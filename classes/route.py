#!/bin/env python

class Route(object):
    def __init__():
        self.routers = []
        self.cost = 0

    def invert(self):
        self.routers = self.routers[::-1]

    def getCost(arg=None):
        if arg is None:
            return self.cost
        if arg is int:
            return

    def __str__(self):
        return "->".join(self.routers)
    def __repr__(self):
        return str(self)
    def __int__(self):
        return self.cost

def main():
    pass


if __name__ == "__main__":
    main()

