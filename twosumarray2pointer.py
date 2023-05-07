#using 2 pointer method --> time complexity = O(n)
class Solution:
    def twoSum(self, numbers: List[int], k: int) -> List[int]:
        f=0  #ppointer 1 starts from front
        b=len(numbers)-1 #pointer 2 starts from last 
        ans=[]
        while(f<b):
            ksum=numbers[f]+numbers[b] #if sum of f and b is less than target value then we need to increment from front
            if ksum<k:
               f+=1
            elif ksum>k: #if sum of f and b is greater than target traverse from back since even if we increment the f we won't be anywhere near to solution logically
                b-=1
            else:
                ans.append(f+1)
                ans.append(b+1)
                break
        return(ans)