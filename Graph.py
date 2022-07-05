class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = dict()
        for edge in edges:
            # this works only if all the edges have been accounted from the perspective of all the vertices in the graph
            if edge[0] in self.graph_dict:
                self.graph_dict[edge[0]].append(edge[1])
            else:
                self.graph_dict[edge[0]] = [edge[1]]
        print("The Graph Dictionary: \n", self.graph_dict)

if __name__ == "__main__":
    pass
else:
    print("Imported Graph\n")