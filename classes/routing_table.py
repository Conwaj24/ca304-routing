#!/bin/env python

from classes.route import Route

class RoutingTable(object):
    def __init__(self):
        self.routes = {}

    def _store_route(self, route):
        routekey = route[-1].name
        if (    routekey not in self.routes or 
                route.cost and
                route.cost < self.routes[routekey]
        ):
            self.routes[routekey] = route

    def add_route(self, *args, cost=None):
        route = Route(*args, cost=cost)
        self._store_route(route)

    def __getitem__(self, index):
        return self.routes[index]
    def __str__(self):
        return str(self.routes)
    def __repr__(self):
        return str(self)

def main():
    pass

if __name__ == "__main__":
    main()

