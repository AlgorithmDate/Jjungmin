n,m=map(int,input().split())
lst=[False for i in range(n+1)]
arr=[0 for i in range(m)]
# 매개변수에 횟수
def backTracking(num):
    if(num==m):
        for i in range(m):
            print(arr[i],end=" ")
        print()
    else:
        for i in range(1,len(lst)):
            if lst[i]==False:
                arr[num]=i
                lst[i]=True
                backTracking(num+1)
                lst[i]=False



backTracking(0)