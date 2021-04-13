def solution(A, F, M):
    dice=[1,2,3,4,5,6]
    # write your code in Python 3.6
    total=M*(F+len(A))
    remaining=total-sum(A)
    
    if F==2:
        return twoSum(remaining,dice)
    if F==1:
        if remaining in dice:
            return [remaining]
        else:
            return [0]
            
    forgotten=kSum(remaining,dice,F,[])
    return forgotten
    
    
    

def kSum(t,dice,k,forgotten):
    if len(dice)==0 or dice[0]*k>t or t>dice[-1]*k:
        return []
    if k==2:
        return twoSum(t,dice)
    for i in range(len(dice)):
        r=kSum(t-dice[i],dice[i+1:],k-1,forgotten)
        # print(r)
        forgotten+=r

    return forgotten
    
    
def twoSum(t,dice):
    seen={}
    for i in range(len(dice)):
        
        diff=t-dice[i]
        if diff in seen:
            return [diff,dice[i]]
        elif diff==dice[i]:
            return [diff,dice[i]]
        else:
            seen[dice[i]]=i
            
    return [0]


a=[]
f=[]
m=[]
print(solution([1, 5, 6], 4, 3))
    