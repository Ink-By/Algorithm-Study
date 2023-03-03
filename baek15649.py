import sys


def DFS():
    if (len(stack) == M):
        print(" ".join(map(str, stack)))
        return
    for i in range(1, N+1):
        if (visit[i]):
            continue
        visit[i] = True
        stack.append(i)
        DFS()

        stack.pop()
        visit[i] = False


N, M = map(int, sys.stdin.readline().split())
stack = []
visit = [False]*(N+1)
DFS()
