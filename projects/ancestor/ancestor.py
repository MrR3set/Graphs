from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesnt exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):

    g = Graph()

    for relation in ancestors:
        g.add_vertex(relation[0])
        g.add_vertex(relation[1])
        g.add_edge(relation[1],relation[0])

    s = Stack()
    s.push([starting_node])

    maxLength = 1
    earliest = -1

    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if (len(path) > maxLength) or v < earliest:
            maxLength=len(path)
            earliest = v
        for next_vertex in g.get_neighbors(v):
            n_path = list(path)
            n_path.append(next_vertex)
            s.push(n_path)
            
    print("Earliest ",earliest)
    print("-"*15)
    return earliest
