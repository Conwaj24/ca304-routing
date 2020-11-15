#!/bin/env python

from classes.router import Router as _Router

class Router(object):
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph
        self.rtr = graph.get_router(name)
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

    def print_routing_table(self):
        print(self.rtr.routing_table)

class Graph(object):
    def __init__(self):
        self.routers = {}

    def get_router(self, name):
        return self.routers[name]

    def add_router(self, name):
        if name not in self.routers:
            self.routers[name] = _Router(name);

    def add_edge(self, start, end, cost):
        self.add_router(start)
        self.add_router(end)
        self.routers[start].add_edge(self.routers[end], cost)

def get_route(graph, a, b):
    return graph.get_router(a).get_path(b)

def main():
    graph = Graph()
    graph.add_edge("a", "b", 7)
    graph.add_edge("a", "c", 9)
    graph.add_edge("a", "f", 14)
    graph.add_edge("b", "c", 10)
    graph.add_edge("b", "d", 15)
    graph.add_edge("c", "d", 11)
    graph.add_edge("c", "f", 2)
    graph.add_edge("d", "e", 6)
    graph.add_edge("e", "f", 9)
    router = Router("a", graph)
    router.rtr.routing_table.explore()
    router.get_path("f")
    router.get_path("e")

    router.print_routing_table()

if __name__ == "__main__":
    main()
