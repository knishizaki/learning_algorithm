import sys
import heapq

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
        for i, v in enumerate(lines):
            if i == 0:
                V = [int(x) for x in v.split()]
                N, M, S = V[0], V[1], V[2]
                route = [[] for x in range(N)]
            else:
                V = [int(x) for x in v.split()]
                route[V[0]].append([V[1],V[2]])

#print(N,M,S,route)

def dijkstra(V, S, e_list):
    inf = 10**9
    done = [False]*V
    dist = [inf]*V
    node_heap = []
    dist[S] = 0
    cur = S

    while True:
        done[cur] = True
        for x in route[cur]:
            if done[x[0]] == False and dist[cur] + x[1] < dist[x[0]]:
                dist[x[0]] = dist[cur] + x[1]
                heapq.heappush(node_heap, [dist[x[0]],x[0]])
        if len(node_heap) == 0:
            return dist
        while node_heap:
            tmp = heapq.heappop(node_heap)[1]
            if done[tmp]== False:
                cur = tmp
                break

for x in dijkstra(N, S, route):
    if x != 10**9:
        print(x)
    else:
        print("INF")
