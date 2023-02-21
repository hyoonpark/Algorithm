from collections import deque

graph = [[0,1,1,0,0,0],
         [1,0,0,1,1,0],
         [1,0,0,0,0,1],
         [0,1,0,0,0,0],
         [0,1,0,0,0,0],
         [0,0,1,0,0,0]]

queue = deque([])    # deque
visited = []    # 방문 확인

def BFS(start_node):
    queue.append(start_node)    # 큐에 시작노드 추가

    while queue:
        node = queue.pop()
        visited.append(node)

        print(node, end=' ')    # 현재 방문한 노드 print

        for i in range(6):
            if graph[node][i] == 1 and i not in visited:
                queue.appendleft(i)

BFS(0)