#!/bin/env python

from classes.route import Route

class RoutingTable(object):
    def __init__(self):
        self.routes = {}
        self.iterable = []

    def route_is_good(self, route):
        routekey = route[-1].name
        return (routekey not in self.routes or
                route.is_valid() and
                route.cost < self.routes[routekey])

    def store_route(self, route):
        self.routes[route[-1].name] = route
        if self.iterable:
            self.iterable.append(route)

    def store_route_if_good(self, route):
        if self.route_is_good(route):
            self.store_route(route)

    def add_route(self, *args, cost=None):
        route = Route(*args, cost=cost)
        self.store_route_if_good(route)

    def explore_route(self, route, force=False):
        if force or self.route_is_good(route):
            self.store_route_if_good(route)
            for r in route[-1].routing_table:
                self.explore_route(route + r)

    def explore(self):
        for route in self:
            self.explore_route(route, force=True)

    def __getitem__(self, index):
        return self.routes[index]
    def __str__(self):
        data=[["","from","to","cost","path"]]+[[len(self.iterable),route[0],route[-1],route.cost,route] for route in self][::-1]
        fmtstr="".join(["{:>"+str(i+1)+"}" for i in [max(col) for col in [[len(str(row[i])) for row in data] for i in range(len(data[0]))]]])
        return "\n".join([fmtstr.format(*[str(e) for e in row]) for row in data])

    def __repr__(self):
        return str(self)
    def __iter__(self):
        self.iterable = [v for v in self.routes.values()]
        return self
    def __next__(self):
        if self.iterable:
            return self.iterable.pop()
        else:
            raise StopIteration

def main():
    pass

if __name__ == "__main__":
    main()

