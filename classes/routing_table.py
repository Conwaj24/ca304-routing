#!/bin/env python

from classes.route import Route

class RoutingTable(object):
    def __init__(self):
        self.routes = {}

    def route_is_good(self, route):
        routekey = route[-1].name
        return (routekey not in self.routes or
                route.cost and
                route.cost < self.routes[routekey])

    def add_route(self, *args, cost=None):
        route = Route(*args, cost=cost)
        if self.route_is_good(route):
            self.routes[route[-1].name] = route

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

