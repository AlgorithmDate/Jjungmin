import sys
n,r,c=map(int,sys.stdin.readline().split())

def func(n,r,c):
    global cnt
    if(n==0):
        return 0
    
    half=(2**(n-1))
    
    #0행 0열부터 시작
    if(r<half and c<half):
        
        func(n-1,r,c)
    elif(r<half and c>=half):
        cnt+=half*half
        func(n-1,r,c-half)+half*half
    elif(r>=half and c<half):
        cnt+=half*half*2
        func(n-1,r-half,c)+2*half*half
    
    elif(r>=half and c>=half):
        cnt+=half*half*3
        func(n-1,r-half,c-half)+3*half*half
    
    return cnt

 
cnt=0
func(n,r,c)
print(cnt)