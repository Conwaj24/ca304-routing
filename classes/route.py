#!/bin/env python

class Route(object):
    def __init__(self, *routers_in_path, cost=None):
        self.path = routers_in_path
        self.subroutes = []
        self.cost = cost
        if cost is None:
            self.calculate(routers_in_path)
            self.clean_dups()
        assert(self.is_valid())

    def calculate(self, routers_in_path):
        if len(routers_in_path) > 1:
            self.subroutes.append( routers_in_path[0].get_path(routers_in_path[1]))
        if len(routers_in_path) > 2:
            self.subroutes.append( Route(*routers_in_path[1:]))
        self.cost = sum([int(r) for r in self.subroutes])

    def inverted(self):
        return Route(
                *self.path[::-1],
                cost=(self.cost if self.is_edge() else None)
            )

    def get_cost(self, arg=None):
        if arg is None:
            return self.cost
        if isinstance(arg, int):
            return

    def is_edge(self):
        return not self.subroutes

    def clean_dups(self):
        if not self.is_edge():
            inds = {}
            i = 0
            while i < len(self.path):
                if self.path[i].name not in inds:
                    inds[self.path[i].name] = i
                else:
                    j = inds[self.path[i].name]
                    self.path = self.path[:j+1] + self.path[i+1:]
                    i = j
                i += 1

    def is_valid(self):
        if self.cost is None:
            return False
        if not self.is_edge():
            prev = self.subroutes[0]
            for route in self.subroutes[1:]:
                if prev[-1] != route[0]:
                    return False
                prev = route
        return True

    def __str__(self):
        return "->".join([str(e) for e in self.path])
    def __repr__(self):
        return str(self)
    def __int__(self):
        return self.cost
    def __len__(self):
        return len(self.path)
    def __getitem__(self, index):
        return self.path[index]
    def __add__(self, other):
        return Route(*self.path, *other.path)
    def __gt__(self, other):
        return int(self) > int(other)
    def __lt__(self, other):
        return int(self) < int(other)

def main():
    pass


if __name__ == "__main__":
    main()
