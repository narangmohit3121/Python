class Vertex(object):
    def __init__(self, vertex_id):
        self._id = vertex_id
        self.connectedTo = {}

    def get_id(self):
        return self._id

    def add_neighbour(self, vertex, cost=0):
        self.connectedTo[vertex] = cost

    def get_connections(self):
        return self.connectedTo.keys()

    def is_connected(self, vertex):
        return vertex in self.connectedTo.keys()

    def get_cost(self, vertex):
        return self.connectedTo[vertex]

    def __str__(self):
        return f"{str(self._id)} connected to {str([vertex._id for vertex in self.connectedTo])} "


class Graph(object):
    def __init__(self):
        self.vertex_list: dict[Vertex] = {}
        self.num_vertices = 0

    def add_vertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertex_list[vertex] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, vertex_id):
        if vertex_id in self.vertex_list:
            return self.vertex_list[vertex_id]
        else:
            return None

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vertex_list:
            new_vertex = Vertex(from_vertex)
            self.vertex_list[from_vertex] = new_vertex

        if to_vertex not in self.vertex_list:
            new_vertex = Vertex(to_vertex)
            self.vertex_list[to_vertex] = new_vertex

        self.vertex_list[from_vertex].add_neighbour(to_vertex, cost)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def __contains__(self, item):
        return item in self.vertex_list.keys()
