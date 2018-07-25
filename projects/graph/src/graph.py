#!/usr/bin/python

import random

"""
Simple graph implementation compatible with BokehGraph class.
"""
"""
# from Monday lecture
# Vertices have a label and a set of edges.
class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()   #vertax = node, edges = pointers.  Set() helps to build the graph list

    #to make it easier to read. without it, it just prints the position index in memory
    def __repr__(self):
        return str(self.label)

class ListGraph:
    # Adjacent lest graph.
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional = True):
        # Add an edge from start to end.
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)
"""

"""
# solution for Part 1

class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        self.vertices = {}  # represent as a dict

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error - adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error - cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges) 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # represent as a dict

    def add_vertex(self, vertex):
        self.vertices[vertex] = set() 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices:
            raise Exception('Error - {} vertices not in graph!'.format(start))
        if end not in self.vertices:
            raise Exception('Error - {} vertices not in graph!'.format(end))
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    """ function to print a BFS of graph"""
    def BFS(self, start):
        visited = [False] * (len(self.vertices))  # mark all the vertices as not visited
        queue = [] # crate a queue for BFS
        queue.append(start) #mark the vertices as visited and enqueue it
        visited[int(start)] = True

        while queue:
            start = queue.pop(0)
            print (start, end=" ")

            for i in self.vertices[start]:
                if visited[int(i)] == False:
                    queue.append(i)
                    visited[int(i)] = True



# need this in order to show the set print in the terminal for part 1
# but once the graph is drawn in draw.py and show in the browser, this section can delete.

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print('Following is BFS start from')
graph.BFS('0')
# graph.add_edge('0', '4')
# graph.add_edge('a', '0')
# graph.add_edge('x', 'y')
print(graph.vertices)


