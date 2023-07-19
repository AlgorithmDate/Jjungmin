import collections
import heapq
import sys



def prim(lst,startNode,visit):
    
    visit[startNode]=True
    candidate=lst[startNode] #배열
    
    heapq.heapify(candidate)

    totalWeight=0
    while(candidate):
  
        cost,x,y=heapq.heappop(candidate)
   
        if(visit[y]==False):
            totalWeight+=cost
            visit[y]=True
    
            for edge in lst[y]:
               #방문노드인지 검사
               if(visit[edge[2]]==False):
                
    
                    heapq.heappush(candidate,edge)


    return totalWeight

while True:
    totalCost=0
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0: #0이 2개 주어질 경우 종료합니다.
        break
    lst = [[] for i in range(m+1)]
    visit=[False]*(m+1)
    for i in range(n):
        x,y,cost=map(int,sys.stdin.readline().split())
        totalCost+=cost
        lst[x].append([cost,x,y])
        lst[y].append([cost,y,x])
    print(totalCost-prim(lst,0,visit))