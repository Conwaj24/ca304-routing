#!/bin/env python

from classes.router import Router as _Router

class Router(object):
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph
        self.rtr = _Router(name)
        pass

    def get_path(self, router_name):
        path = self.rtr.get_path(router_name)
        print("""Start: {}\nEnd: {}\nPath: {}\nCost: {}""".format(
                self.name,
                router_name,
                path,
                path.cost
            )
        )

class Graph(object):
    def __init__(self):
        self.routers = {}

    def add_router_if_new(self, name):
        if name not in self.routers:
            self.routers[name] = _Router(name);

    def add_router(self, start, end, cost):
        self.add_router_if_new(start)
        self.add_router_if_new(end)
        self.routers[start].add_edge(self.routers[end], cost)

def main():
    graph = Graph()
    graph.add_router("a", "b", 7)
    graph.add_router("a", "c", 9)
    graph.add_router("a", "f", 14)
    graph.add_router("b", "c", 10)
    graph.add_router("b", "d", 15)
    graph.add_router("c", "d", 11)
    graph.add_router("c", "f", 2)
    graph.add_router("d", "e", 6)
    graph.add_router("e", "f", 9)
    router = Router("a", graph)
    router.get_path("f")

if __name__ == "__main__":
    main()

