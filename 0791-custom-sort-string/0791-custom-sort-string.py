class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #to get the count of each element in string 's'
        temp={}
        for ele in s:
            temp[ele]=1+temp.get(ele,0)
        
        res=[]
        #making our result based on the 'order' string
        for ele in order:
            if ele in temp:
                res.append(ele*temp[ele])
                temp[ele]=0
        #for those elements that remain in s as not in order
        for x in temp:
            if temp[x]!=0:
                res.append(x*temp[x])

        ans=''.join(res)
        return ans
        