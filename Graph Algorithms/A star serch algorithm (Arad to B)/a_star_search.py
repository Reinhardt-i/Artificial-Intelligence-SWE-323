class Graph:
    H = {}

    def __init__(self, _adjacency_list, heuristics):
        self.adjacency_list = _adjacency_list
        self.H = heuristics

    def neighbors(self, v):
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node):

        list1, list2, guess, par = {start_node}, set([]), {start_node: 0}, {start_node: start_node}

        while len(list1) > 0:
            n = None

            for v in list1:
                if n is None or guess[v] + self.H[v] < guess[n] + self.H[n]:
                    n = v

            if n is None:
                print("NO PATH FOUND")
                return None

            if n == stop_node:
                path_to_take = []
                while par[n] != n:
                    path_to_take.append(n)
                    n = par[n]
                path_to_take.append(start_node)
                path_to_take.reverse()
                for path in path_to_take:
                    print(f"{path} -> ", end=" ")
                print("We reached to the Destination!")
                return path_to_take

            for (m, weight) in self.neighbors(n):
                if m not in list1 and m not in list2:
                    list1.add(m)
                    par[m] = n
                    guess[m] = guess[n] + weight
                else:
                    if guess[m] > guess[n] + weight:
                        guess[m] = guess[n] + weight
                        par[m] = n

                        if m in list2:
                            list2.remove(m)
                            list1.add(m)
            list1.remove(n)
            list2.add(n)

        print("NO PATH FOUND")
        return None


if __name__ == '_main_':

    adj_list, Heuristics_of_adj_list = {}, {}

    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            i, node, heu_node = 0, 0, 0
            last_node, last_val = "", 0
            for word in line.split():
                if i == 0:
                    node = word
                    adj_list[node] = []
                elif i == 1:
                    heu_node = int(word)
                    Heuristics_of_adj_list[node] = heu_node
                elif i % 2 == 0:
                    last_node = word
                else:
                    last_val = int(word)
                    current_tuple = (last_node, last_val)
                    adj_list[node].append(current_tuple)
                i += 1

    Graph(adj_list, Heuristics_of_adj_list).a_star_algorithm('Arad', 'Bucharest')