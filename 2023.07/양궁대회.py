from itertools import combinations_with_replacement
def solution(n,info):
   
    answer=[-1]
    maxCount=0
    # 중복조합
    for cwr in combinations_with_replacement(range(11),n):
        info2=[0]*11
       
        for num in cwr:
            info2[10-num]+=1
        apeach=0
        ryan=0
        for i in range(11):
            if info[i]==info2[i]==0:
                continue
            #10-i로 넣어줘야함!
            elif(info[i]>=info2[i]):
                apeach+=10-i
            else:
                ryan+=10-i
        if(ryan>apeach): # 라이언은 어피치 보다 무조건 커야함
            if(ryan-apeach>maxCount):
                maxCount=ryan-apeach
                answer=info2


                        
    return answer
    
        
        
    
    
        
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))

# cwr=list(combinations_with_replacement([i for i in range(1,11)],5))
# print(cwr)