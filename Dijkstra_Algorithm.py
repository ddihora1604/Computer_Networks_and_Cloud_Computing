import sys

# Function to find the vertex with the minimum distance that has not yet been visited
def min_distance(dist, visited, size):
    min_val = sys.maxsize
    min_index = -1
    for v in range(size):
        if visited[v] == 0 and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index

# Function to relax edges and update the parent array
def relax(graph, u, dist, parent, visited, size):
    for v in range(size):
        if not visited[v] and graph[u][v] != 0 and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
            dist[v] = dist[u] + graph[u][v]
            parent[v] = u

# Dijkstra's algorithm to find the shortest paths from the source vertex
def dijkstra(graph, source, size):
    dist = [sys.maxsize] * size
    visited = [0] * size
    parent = [-1] * size  # Array to store the shortest path tree
    dist[source] = 0

    for _ in range(size - 1):
        u = min_distance(dist, visited, size)
        visited[u] = 1
        relax(graph, u, dist, parent, visited, size)

    print("Vertex\tDistance from Source\tPath")
    for i in range(size):
        print(f"{i}\t\t{dist[i]}\t\t\t{get_path(parent, i)}")

# Function to reconstruct the path using the parent array
def get_path(parent, vertex):
    path = []
    while vertex != -1:
        path.append(vertex)
        vertex = parent[vertex]
    return " -> ".join(map(str, path[::-1]))

# Main function to take user input and run Dijkstra's algorithm
def main():
    V = int(input("Enter the number of vertices: "))
    graph = [[0 for _ in range(V)] for _ in range(V)]

    E = int(input("Enter the number of edges: "))
    print("Enter edges in the format (source, destination, weight):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w  # Assuming it's an undirected graph

    source = int(input("Enter the source vertex: "))
    dijkstra(graph, source, V)

# Run the program
if __name__ == "__main__":
    main()
