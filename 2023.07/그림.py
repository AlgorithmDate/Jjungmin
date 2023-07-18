from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[False]*m]*n

def bfs(graph,startX,startY):
    queue=deque()
    queue.append((startX,startY))
    graph[startX][startY]=0  # 굳이 visited배열이 필요 없음
    area=1
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
           
            nx=x+dx[i]
            ny=y+dy[i]
            
            if(nx>=0 and nx<n and ny>=0 and ny<m):
                if(graph[nx][ny]==1):
                    #print(nx,ny)
                    queue.append((nx,ny))
                    graph[nx][ny]=0
                    area+=1

    
    return area


cnt=0
maxArea=0
for i in range(n):
    for j in range(m):
        if(graph[i][j]==1):
            cnt+=1
            area=bfs(graph,i,j)
            if(area>maxArea):
                maxArea=area

print(cnt)
print(maxArea)  
            