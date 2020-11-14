#!/bin/env python

from classes.routing_table import RoutingTable

class Router(object):
    def __init__(self, name):
        self.name=name
        self.routes = RoutingTable()
        self.add_edge(self, 0)

    def add_edge(self, to, cost):
        self.routes.add_route(self, to, cost=cost)

    def get_path(self, to):
        if isinstance(to, Router):
            return self.routes[to.name]
        return self.routes[to]

    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

def main():
    pass

if __name__ == "__main__":
    main()

