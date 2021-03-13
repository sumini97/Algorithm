# N×M크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
N,M = map(int, input().split())
s = []
q = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    s.append(list(input()))
q = [[0, 0]]

s[0][0] = 1 
while q:
    a, b = q[0][0], q[0][1]
    del q[0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < N and 0 <= ny < M and s[nx][ny] == "1":
            q.append([nx, ny])
            s[nx][ny] = s[a][b] + 1
print(s[N - 1][M - 1])