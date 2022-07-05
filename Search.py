class Search_Algorithms:
    
    def dfs(graph_dict: dict, start: str) -> str:
        seen = set()
        active_stack = list()
        dfs_output = list()
        active_stack.append(start)
        while len(active_stack) > 0:
            node = active_stack.pop()
            if node not in seen:
                seen.add(node)
                dfs_output.append(node)
                neighbors = graph_dict[node]
                for neighbor in neighbors:    
                    active_stack.append(neighbor)
        output = "--".join(dfs_output)
        return output

    def bfs(graph_dict: dict, start: str) -> str:
        seen = set()
        active_queue = list()
        bfs_output = list()
        active_queue.insert(0,start)
        while len(active_queue) > 0:
            node = active_queue.pop()
            if node not in seen:
                seen.add(node)
                bfs_output.append(node)
                neighbors = graph_dict[node]
                for neighbor in neighbors:
                    active_queue.insert(0,neighbor)
        output = "--".join(bfs_output)
        return output

if __name__ == "__main__":
    pass
else:
    print("Imported Search Algorithms\n")