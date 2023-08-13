n,s=map(int,input().split())
cnt=0
arr = list(map(int, input().split()))

def backTracking(num,sum):
    global cnt
    if(num==n):
      return
    sum+=arr[num]
    if(sum==s):
      cnt+=1
    else:
       
        backTracking(num+1,sum)
        backTracking(num+1,sum-arr[num])
backTracking(0,0)
print(cnt)