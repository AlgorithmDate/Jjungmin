import heapq
import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,k=map(int,sys.stdin.readline().split())
lst=[]
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

s,x,y=map(int,sys.stdin.readline().split())


def infection(s,x,y):

    while(s!=0):
        if(lst[x-1][y-1]!=0):
            return lst[x-1][y-1]
        else:
             s-=1
             bfs(x-1,y-1)
  
    #print(lst)
    return lst[x-1][y-1]


def bfs(targetX,targetY):

    if(lst[targetX][targetY]!=0):
        return


    heap=[]
    for i in range(n):
        for j in range(n):
            if(lst[i][j]!=0):
                heapq.heappush(heap,(lst[i][j],i,j))


    while(heap):
        if(lst[targetX][targetY]!=0):
            break

        data,x,y=heapq.heappop(heap)
        

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(lst[nx][ny]==0):
                    lst[nx][ny]=data
 
    
            
print(infection(s,x,y))