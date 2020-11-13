#!/bin/env python

from classes.routing_table import RoutingTable

class Router(object):
    NAMETYPE = str
    def __init__(self, name: NAMETYPE):
        self.name=name
        self.routes = RoutingTable()

    def add_edge(self, to, cost):
        self.routes.add_route(self, to, cost)

    def get_path(self, to):
        return self.routes[to]

def main():
    pass

if __name__ == "__main__":
    main()

