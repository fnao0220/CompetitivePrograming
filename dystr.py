import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # 初期化
    shortest_paths = {node: (None, float('inf')) for node in graph}
    shortest_paths[start] = (None, 0)
    visited = set()
    current_node = start
    
    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        current_weight = shortest_paths[current_node][1]
        
        for next_node, weight in destinations.items():
            weight += current_weight
            if weight < shortest_paths[next_node][1]:
                shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in graph if node not in visited}
        if not next_destinations:
            break
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    return shortest_paths

def draw_graph(graph, shortest_paths, start):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for dest, weight in edges.items():
            G.add_edge(node, dest, weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrowsize=20)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    for node in shortest_paths:
        path = []
        current = node
        while current is not None:
            path.append(current)
            next_node = shortest_paths[current][0]
            current = next_node
        path = path[::-1]
        path_edges = [(path[n], path[n+1]) for n in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    plt.title('Dijkstra Algorithm')
    plt.show()

# グラフの定義
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
draw_graph(graph, shortest_paths, start_node)
