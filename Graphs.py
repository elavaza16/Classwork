import heapq # priorities - provides a priority queue
class Graph:
    def __init__(self,directed=False):
        self.directed=directed

        self.adj_list=dict() # dict to store the graph


    def insert(self):
        pass
    #Dunder
    def __repr__(self):
        #Initialise an empty string
      graph_str= ""
      #Key-node,neighbours-Tuple
      for node, neighbours in self.adj_list.items():
          graph_str+=f"{node}->{neighbours}\n"
      return graph_str

    def obtain_neighbours(self,node):

        return self.adj_list.get(node,set())

    ## Added this
    def get_nodes(self):
        return list(self.adj_list.keys())

    def adj_matrix(self):
        nodes = self.get_nodes()

        index = {node:i for i, node in enumerate(nodes)}
        size=len(nodes)
        matrix = [[0 for _ in range(size)]for _ in range(size)]
        for from_node, neighbours in self.adj_list.items():
            for neighbour in neighbours:
                if isinstance(neighbour,tuple): ##to_node to neighbour??
                    to,weight=neighbour
                    matrix[index[from_node]][index[to]]=weight
                else:
                    matrix [index[from_node]][index[neighbour]]=1
        return matrix


    def add_node(self,node):

        if node not  in self.adj_list:
            self.adj_list[node]=set()

        else:
            raise ValueError("The Node already exists")


    def add_edge(self,from_node ,to_node, weight=None):

        if from_node not in self.adj_list:

            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
#Weight is none
            self.adj_list[from_node].add(to_node)

            if not self.directed:

             self.adj_list[to_node].add(from_node)

#If there is a weight
        else:
            self.adj_list[from_node].add((to_node,weight))


        if not self.directed:
            self.adj_list[to_node].add((from_node,weight))



    def depth_first_search(self,start):

        visited=set()
        stack=[start]
        order=[]

        while stack:
            node=stack.pop() # removed 0

            if node not in visited:
                visited.add(node)
                order.append(node)


            neighbours=self.obtain_neighbours(node)

            for neighbour in neighbours:
                if isinstance(neighbour,tuple):
                    neighbour =neighbour[0]

                if neighbour not in visited:
                    stack.append(neighbour)

        return order


    def breadth_first_search(self,start):

        visited=set()
        queue=[start]
        order=[]

        while queue:
            node=queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours=self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour,tuple):
                        neighbour=neighbour[0]

                    if neighbour not in visited:
                        queue.append(neighbour)
        return order


    def dijkstra(self, start):
        distances = {node: float('inf')for node in self.adj_list}
        distances[start]=0

        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour in self.obtain_neighbours(current_node):
                if isinstance(neighbour, tuple):
                    neighbour_node, weight = neighbour
                else:
                    neighbour_node = neighbour
                    weight = 1

                if neighbour_node in visited:
                    continue

                distance = current_distance + weight
                if distance < distances[neighbour_node]:
                    distances[neighbour_node] = distance
                    heapq.heappush(priority_queue, (distance, neighbour_node))

        return distances


if __name__=='__main__':

    graph_obj=Graph(False)
    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","C",24)
    graph_obj.add_edge("B","D",50)
    graph_obj.add_edge("C","D")

    print("Graph:")
    print(graph_obj)
    print("DFS SEARCH YIELDS: ",graph_obj.depth_first_search("A"))
    print("BFS SEARCH YIELDS: ",graph_obj.breadth_first_search("A"))

    print("\nAdjacency Matrix:")
    for row in graph_obj.adj_matrix():
        print(row)

    print("\nDijkstra's shortest paths from A:")
    shortest_paths = graph_obj.dijkstra("A")
    for node, distance in shortest_paths.items():
        print(f"A -> {node}: {distance}")

