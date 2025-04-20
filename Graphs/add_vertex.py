class Graph:
    def __init__(self):
        self.adj_lst= {}
    def add_vertex(self,vertex):
        if vertex not in self.adj_lst.keys():
            self.adj_lst[vertex] = []
            return True
        return False
    def print_graph(self):
        for vertex in self.adj_lst:
            print(vertex,":", self.adj_lst[vertex])
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()