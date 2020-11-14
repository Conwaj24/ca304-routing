#!/bin/env python

from classes.routing_table import RoutingTable

class Router(object):
    def __init__(self, name):
        self.name=name
        self.routing_table = RoutingTable()
        self.add_edge(self, 0)
        #self.routing_table.explore()

    def add_edge(self, to, cost):
        self.routing_table.add_route(self, to, cost=cost)

    def get_path(self, to):
        if isinstance(to, Router):
            return self.routing_table[to.name]
        return self.routing_table[to]

    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

def main():
    pass

if __name__ == "__main__":
    main()
