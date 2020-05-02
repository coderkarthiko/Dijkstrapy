import heapq as hq


class Graph:
    L, D = [], []
    N, M = 0, 0

    def get(self):
        self.N, self.M = [int(y) for y in input().split()]
        self.L.extend([[] for y in range(self.N)])
        for k in range(self.M):
            u, v, w = [int(y) for y in input().split()]
            self.L[u].append([w, v])
            self.L[v].append([w, u])

    def dijkstra(self, src):
        self.D, v, heap = [2147483647] * self.N, [False] * self.N, [[0, src]]
        self.D[src] = 0
        while len(heap):
            src = heap[0][1]
            for p in self.L[src]:
                self.D[p[1]] = min(self.D[p[1]], self.D[src] + p[0])
                if not (v[p[1]]):
                    hq.heappush(heap, p)
                    v[p[1]] = True
            hq.heappop(heap)


g = Graph()
g.get()
for i in range(g.N):
    g.dijkstra(i)
    for d in g.D:
        print(d, end=" ")
    print()
