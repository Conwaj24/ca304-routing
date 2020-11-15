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

    def is_valid(self):
        return all([route.is_valid() for route in self])

    def explore_route(self, route, force=False):
        if force or self.route_is_good(route):
            self.store_route_if_good(route)
            for r in route[-1].routing_table:
                self.explore_route(route + r)

    def explore(self):
        for route in self:
            self.explore_route(route, force=True)

    def selftest(self):
        if not self.is_valid():
            self.explore()

    def __getitem__(self, index):
        return self.routes[index]
    def __str__(self):
        #It's beautiful, isn't it? :')
        return(lambda d:(lambda d,f:"\n".join([f.format(*[str(e)for e in r])for r in d]))(d,"".join(["{:>"+str(i+1)+"}"for i in [max(c)for c in[[len(str(r[i]))for r in d]for i in range(len(d[0]))]]])))([["","from","to","cost","path"]]+[[len(self.iterable),r[0],r[-1],r.cost,r]for r in self][::-1])

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

