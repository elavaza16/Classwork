class Graph:
    def _init_(self,directed=False):
        self.directed=directed

        self.adj_list=dict()


    def insert(self):
        pass
    #Dunder
    def _repr_(self):
        #Initialise an empty string
      graph_str= ""
      #Key-node,neighbours-Tuple
      for node, neighbours in self.adj_list:

          graph_str+=f"{node}->{neighbours}\n"

          return graph_str

    def obtain_neighbours(self,node):

        return self.adj_list(node,set())

    def adj_matrix(self):
        pass

    def add_node(self,node):

        if node not  in self.adj_list:
            self.adj_list[node]=set()

        else:
            raise "The Node already exists"


    def add_edge(self,from_node ,to_node, weight=None):

        if from_node not in self.adj_list:

            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
#Weight is none
            self.adj_list[from_node].add[to_node]

            if not self.directed:

             self.adj_list[to_node].add[from_node]

#If there is a weight
        else:
            self.adj_list[from_node].add[(to_node,weight)]


        if not self.directed:
            self.adj_list[to_node].add[(from_node,weight)]



    def depth_first_search(self,start):

        visited=set()
        stack=[start]
        order=[]

        while stack:
            node=stack.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)


            neighbours=self.obtain_neighbours(node)

            for neighbour in neighbours:
                if isinstance(neighbour,tuple):
                    neighbours=neighbour[0]

                if neighbour not in visited:
                    stack.append(neighbour)

        return order


    def breadth_first_search(self,start):

        visited=set()
        queue=[start]
        order=[]

        while queue:
            node=queue.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours=self.obtain_neighbours(node)

                for neighbour in neighbours(node):
                    if isinstance(neighbour,tuple):
                        neighbours=neighbour[0]

                    if neighbour not in visited:
                        queue.append(neighbour)


        return order



if __name__=='main_':

    graph_obj=Graph(False)
    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","C",24)
    graph_obj.add_edge("B","D",50)
    graph_obj.add_edge("C","D")

    print(graph_obj)
    print("DFS SEARCH YIELDS: ",graph_obj.depth_first_search("A"))
    print("BFS SEARCH YIELDS: ",graph_obj.breadth_first_search("A"))

    #
    # print("DJIKSTRA:")
    # print("Shortest path")