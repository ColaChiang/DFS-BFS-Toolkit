from collections import deque

class ShortestPath:
    def __init__(self, graph):
        self.graph = graph  # 圖結構
    
    def bfs_shortest_path(self, start, end):
        queue = deque([(start, [start])])
        visited = set()
        
        while queue:
            node, path = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return path
            for neighbor in self.graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))
        return f"無法從 {start} 到 {end}"
