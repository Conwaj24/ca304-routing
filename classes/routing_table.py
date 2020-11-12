#!/bin/env python

from classes.route import Route

class RoutingTable(object):
    def __init__(self):
        self.routes = {}

    def _store_route(self, route):
        routekey = route[0].name
        if (    routekey in self.routes and 
                route.cost and
                route.cost < self.routes[routekey]
        ):
            self.routes[routekey] = route

    def add_route(self, *args, cost=None):
        route = Route(*args)
        if cost:
            route.cost = cost
        self._store_route(route)

    def __getitem__(self, index):
        return self.routes[index]

def main():
    pass

if __name__ == "__main__":
    main()

