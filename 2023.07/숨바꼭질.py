from collections import deque
n,k=map(int,input().split())
MAX=100001
lst=[0]*(MAX)
def bfs(a):
    queue=deque()
    queue.append(a)
    while(queue):
        node=queue.popleft()
        if(node==k):
            return lst[node]
        # 따로 cnt 같은 변수를 두는게 아니라 인접한 애에서 +1 이렇게 가는거 
        # 그니까 lst[next_node]=lst[node]+1 이 된다
        for next_node in (node-1,node+1,node*2):
                # 0<= <10000 이라는 범위 안에 있어야 하며 방문하지 않았어야 함
                if next_node>=0 and next_node<MAX and lst[next_node]==0:
                    lst[next_node]=lst[node]+1
                    queue.append(next_node)

print(bfs(n))