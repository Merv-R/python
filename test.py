from Graph import Graph
from Search import Search_Algorithms

if __name__ == "__main__":
    routes = [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("A", "E"),
        ("B", "A"),
        ("B", "C"),
        ("B", "G"),
        ("C", "A"),
        ("C", "B"),
        ("C", "D"),
        ("D", "A"),
        ("D", "C"),
        ("D", "E"),
        ("D", "H"),
        ("E", "A"),
        ("E", "D"),
        ("E", "F"),
        ("F", "E"),
        ("F", "H"),
        ("F", "G"),
        ("G", "B"),
        ("G", "F"),
        ("H", "D"),
        ("H", "F")     
    ]
    route_graph = Graph(routes)
    start_node = "A"
    print(Search_Algorithms.dfs(route_graph.graph_dict, start_node))
    print(Search_Algorithms.bfs(route_graph.graph_dict, start_node))
