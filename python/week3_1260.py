# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# DFS

N,M,V=map(int, input().split())

home= [[0]*(N+1) for i in range(N+1)] # 0
for i in range(M):
    linked1, linked2 =map(int, input().split())
    home[linked1][linked2]= home[linked2][linked1]=1
visited=[0]*(N+1)


def DFS(V):
    visited[V]=1 # 방문한 정점 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if visited[i] == 0 and home[V][i] == 1: #방문한 적이 없고 간선으로 연결되어 있다면 1로 표시
            DFS(i) # 재귀

def BFS(V):
    q=[V] # 큐에 저장
    visited[V]=0 # DFS에서는 방문한 곳을 1로 표현하였기에 이를 다르게 하기 위해 0으로 설정
    while q:
        V=q.pop(0) # 큐는 선입선출
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited[i]==1 and home[V][i]==1): # 방문한 적이 없고 간선으로 연결되어 있으면
                q.append(i) # 해당 값을 큐에 저장
                visited[i]=0 # 해당 점을 방문하였다고 표시

DFS(V)
print()
BFS(V)