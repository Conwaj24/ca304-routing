#!/bin/env python

class Route(object):
    def __init__(self, *routers_in_path, cost=None):
        self.path = routers_in_path
        self.subroutes = []
        if cost:
            self.cost = cost
        else:
            self.calculate(routers_in_path)

    def calculate(self, *routers_in_path):
        if len(routers_in_path) > 1:
            self += (
                    routers_in_path[0].get_path(routers_in_path[1]) +
                    Route(routers_in_path[1:])
            )

    def invert(self):
        self.calculate(*self.path[::-1])

    def get_cost(self, arg=None):
        if arg is None:
            return self.cost
        if arg is int:
            return

    def is_edge(self):
        return not self.subroutes

    def is_valid(self):
        """return true if all of the subroutes connect together"""
        if not self.is_edge():
            prev - self.subroutes[0]
            for route in self.subroutes[1:]:
                if prev[-1] != route[0]:
                    return False
                prev = route
        return True

    def __str__(self):
        return "->".join(self.path)
    def __repr__(self):
        return str(self)
    def __int__(self):
        return self.cost
    def __len__(self):
        return len(self.path)
    def __getitem__(self, index):
        return self.path[index]
    def __add__(self, other):
        return Route(self.path + other.path)
    def __iadd__(self, other):
        self.path += other.path
        self.subroutes += other.subroutes
        self.cost += other.cost
        assert(self.is_valid)
        return self

def main():
    pass


if __name__ == "__main__":
    main()
