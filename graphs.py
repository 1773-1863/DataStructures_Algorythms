# consist of vertexes and connections(edges)
# edges can be weighted and non-weighted
# edges can be directional and bidirectional
# adjacency matrix = if connection between two vertex = 1, else = 0
# adjacency list = { "A" : ["B", "E"] } ==  A connected to the vertexes  B and E
# BIG O of GRAPHS
    # adding a vertex to the matrix: an extra row and columns will be added to the matrix
    # so operation is eveluated with O(V^2)
    # adding a vertex to the adjacency JSON is O(1)
    #adding an edge == O(1)


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex,":", self.adj_list[vertex])

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edges in self.adj_list[vertex]:
                self.adj_list[edges].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


print("-----------------------  INIT / GRAPHS -----------------------")
my_graph = Graph()
print("-----------------------  ADD VERTEX / GRAPHS -----------------------")
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
print("-----------------------  PRINT GRAPH / GRAPHS -----------------------")
my_graph.print_graph()
print("-----------------------  ADD AN EDGE / GRAPHS -----------------------")
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 1)
my_graph.print_graph()
print("-----------------------  REMOVE AN EDGE / GRAPHS -----------------------")
my_graph.remove_edge(1, 4)
my_graph.print_graph()
print("-----------------------  REMOVE A VERTEX / GRAPHS -----------------------")
my_graph.remove_vertex(2)
my_graph.remove_vertex(4)
my_graph.print_graph()
