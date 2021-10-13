from collections import OrderedDict
import enum


class VisitedState(enum.Enum):
    unvisited = 1
    visited = 2
    explored = 3


# vertex is being referred to node here
class Node(object):
    def __init__(self, node_id):
        self.id = node_id
        self.adjacencts = OrderedDict()
        self.visitedState = VisitedState.unvisited

    def add_connection(self, node, cost=0):
        new_connection = Node(node)
        self.adjacencts[new_connection] = cost


class Graph(object):
    def __init__(self):
        self.vertex_list = OrderedDict()

    def add_edge(self, from_node, to_node, cost=0):
        # vertex is being referred to node here
        if from_node not in self.vertex_list:
            new_node = Node(from_node)
            self.vertex_list[to_node] = new_node
        if to_node not in self.vertex_list:
            new_node = Node(to_node)
            self.vertex_list[to_node] = new_node
        self.vertex_list[to_node].add_connection(to_node, cost)


# g = Graph()
# g.add_edge('A', 'B')


def breadth_first_search(graph, start):
    # vertex is being referred to node here
    visited_nodes = set()
    search_queue = [start]

    while search_queue:
        # vertex is being referred to node here
        current_node = search_queue.pop(0)
        print(current_node)
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            for node in graph[current_node] - visited_nodes:
                search_queue.append(node)

    # print(visited_nodes)
    return visited_nodes


def breadth_first_search_with_ordered_dict(graph, start):
    # vertex is being referred to node here
    visited_nodes = OrderedDict()
    search_queue = [start]

    while search_queue:
        # vertex is being referred to node here
        current_node = search_queue.pop(0)
        if current_node not in visited_nodes:
            visited_nodes[current_node] = None
            for node in graph[current_node] - set(visited_nodes.keys()):
                search_queue.append(node)

    print(visited_nodes.keys())
    return visited_nodes


def find_all_paths_bfs(graph, start, goal):
    search_queue = [(start, [start])]
    while search_queue:
        node, path = search_queue.pop(0)
        for next_node in graph[node] - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                search_queue.append((next_node, path + [next_node]))


def depth_first_search(graph, start):
    visited = set()
    search_stack = [start]
    while search_stack:
        # vertex is being referred to node here
        current_node = search_stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            search_stack.extend(graph[current_node] - visited)
    print(visited)
    return visited


def depth_first_search_with_ordered_dict(graph, start):
    visited = OrderedDict()
    search_stack = [start]
    while search_stack:
        # vertex is being referred to node here
        current_node = search_stack.pop()
        if current_node not in visited.keys():
            visited[current_node] = None
            search_stack.extend(graph[current_node] - set(visited.keys()))

    print(visited.keys())
    return visited.keys()


def find_shortest_path_between_vertices(graph):
    paths_between_vertices = {}
    for start_vertex in graph:
        for end_vertex in graph:
            if start_vertex != end_vertex:
                current_combo = start_vertex + end_vertex
                paths_between_vertices[current_combo] = []
                for path in find_all_paths_bfs(graph, start_vertex, end_vertex):
                    if (len(path) < len(paths_between_vertices[current_combo])) or \
                            len(paths_between_vertices[current_combo]) == 0:
                        paths_between_vertices[current_combo] = path
                    # paths_between_vertices[current_combo].append(path)

    return paths_between_vertices


t = 0
d = 0


def find_articulation_points(graph, current_vertex, low={}, disc={}, visited=[], ap={}, parent={}, root=""):
    global t
    global d
    if root == "":
        root = current_vertex
    children = 0
    visited.append(current_vertex)
    low[current_vertex] = t+1
    disc[current_vertex] = d+1
    for conn in graph[current_vertex]:
        if conn not in visited:
            children += 1
            parent[conn] = current_vertex
            find_articulation_points(graph, conn, low, disc, visited, ap, parent, root)
            low[current_vertex] = min(low[current_vertex, low[conn]])
            if low[current_vertex] >= disc[current_vertex]:
                ap[current_vertex] = True
        elif conn != parent[current_vertex]:
            low[current_vertex] = min(low[current_vertex], low[conn])
    return ap


g2 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'E', 'C'},
}
# breadth_first_search(g2, 'A')
# breadth_first_search_with_ordered_dict(g2, 'A')
# all_paths_A_F = list(find_all_paths_bfs(g2, 'A', 'F'))
# print(all_paths_A_F)
# depth_first_search_with_ordered_dict(g2, 'A')
print(find_shortest_path_between_vertices(g2))


###########################################################################################################
def word_ladder(wordlist):
    word_graph = Graph()
    buckets = {}
    connections = {}
    for word in wordlist:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[(i+1):]
            if bucket in buckets:
                buckets[bucket].add(word)
            else:

                buckets[bucket] = {word}

    for current_bucket in buckets:
        words_in_bucket = buckets[current_bucket]
        for word1 in words_in_bucket:
            for word2 in words_in_bucket:
                if word1 != word2:
                    word_graph.add_edge(word1, word2)
                    # dictionary representation of the graph
                    if word1 in connections:
                        connections[word1].add(word2)
                    else:
                        connections[word1] = {word2}
    # print(buckets)
    # print(connections)
    return word_graph


word_ladder(['POOL', 'FOOL', 'COOL', 'COAL', 'FOAL', 'POLL', 'POLE'])
word_graph_1 = {
    'POOL': {'POLL', 'FOOL', 'COOL'},
              'FOOL': {'FOAL', 'POOL', 'COOL'},
              'COOL': {'POOL', 'FOOL', 'COAL'},
              'POLL': {'POOL', 'POLE'},
              'FOAL': {'FOOL', 'COAL'},
              'COAL': {'FOAL', 'COOL'},
              'POLE': {'POLL'}
              }
# print(list(find_all_paths_bfs(word_graph_1, 'FOOL', 'POLE')))

