
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for i in range(n)]

dp[0][0]=lst[0][0]
for i in range(1,n):
    for j in range(len(lst[i])):
            
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+lst[i][j]
            

print(max(dp[n-1]))