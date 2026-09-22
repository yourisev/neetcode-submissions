from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def edgesToAdjList(edges):

            adj = defaultdict(list)

            for u,v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            return adj
        
        def detectCycle(adj, vis, node, parent):

            vis.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                elif neighbor in vis:
                    return True
                elif detectCycle(adj, vis, neighbor, node):
                    return True

            return False

        
        visited =  set()
        adjList = edgesToAdjList(edges)

        tmp =  detectCycle(adjList, visited, 0, -1)

        return False if len(visited) != n or tmp else True