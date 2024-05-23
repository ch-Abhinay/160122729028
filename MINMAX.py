import math
def minimax(cd,ni,mt,scores,td):
    if cd==td:
        return scores[ni]
    if mt:
        return max(minimax(cd+1,ni*2,False,scores,td), minimax(cd+1,ni*2+1,False,scores,td))
    else:
        return min(minimax(cd+1,ni*2,True,scores,td), minimax(cd+1,ni*2+1,True,scores,td))
scores=[1,2,3,4,5,6,7,8]
print(minimax(0,0,True,scores,math.log(len(scores),2)))