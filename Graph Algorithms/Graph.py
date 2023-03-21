import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start_node, end_node, cost):
        if start_node not in self.edges:
            self.edges[start_node] = []
        self.edges[start_node].append((end_node, cost))

    def get_neighbors(self, node):
        if node in self.edges:
            return self.edges[node]
        return []

    def __str__(self):
        return str(self.edges)

    def heuristic(self, node, goal):
        dict_h = {
            'A' : 100,
            'B' : 200,
            'C' : 300,
            'D' : 0            
        }
        return dict_h[node]

    def a_star_search(self, graph, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for neighbor, cost in graph.get_neighbors(current):
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path, cost_so_far[goal]




graph = Graph()
graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'D', 5)
graph.add_edge('B', 'C', 1)


path, cost = graph.a_star_search(graph, 'A', 'D')
print("Shortest path:", path)
print("Total cost:", cost)