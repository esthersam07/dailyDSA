class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #monotonic stack
        #monotonic increase
        #take an empty stack
        #add an element if the element before is less than the one being added
        #if not, remove previous, decrement value of k, and check with the previous again
        stack = []
        for i in num:
            while(stack!=[] and i<stack[-1] and k>0):
                del stack[-1]
                k-=1
            stack.append(i)
        #this is done if the given num is already in increasing order and at the end none of the elements are removed, then delete k elements from the end
        stack = stack[:len(stack)-k]
        
        res = "".join(stack).lstrip("0")
        return str(res) if res else "0"  
        