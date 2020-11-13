#!/bin/env python

class Route(object):
    def __init__(self, *routers_in_path, cost=None):
        self.path = []
        if cost:
            self.path=routers_in_path
            self.cost = cost
        else:
            self.calculate(routers_in_path)
        self.is_edge = len(self.path) == 1

    def calculate(self, *routers_in_path):
        if len(routers_in_path) > 1:
            self += (
                    routers_in_path[0].get_path(routers_in_path[1]) +
                    Route(routers_in_path[1:])
            )

    def invert(self):
        self.path = self.path[::-1]

    def get_cost(self, arg=None):
        if arg is None:
            return self.cost
        if arg is int:
            return

    def __str__(self):
        return "->".join(self.path)
    def __repr__(self):
        return str(self)
    def __int__(self):
        return self.cost
    def __len__(self):
        return len(self.path) + 1

def main():
    pass


if __name__ == "__main__":
    main()
