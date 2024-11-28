from queue import Queue
def BFS_AL (vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty() :
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True

vtx = ['U','V','W','X','Y']
aList=[[1, 2],
       [0, 2, 3],
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx, aList, 0)
print()
