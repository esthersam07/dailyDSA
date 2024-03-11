class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp={}
        for ele in s:
            temp[ele]=1+temp.get(ele,0)

        res=[]
        for ele in order:
            if ele in temp:
                res.append(ele*temp[ele])
                temp[ele]=0

        for x in temp:
            if temp[x]!=0:
                res.append(x*temp[x])

        ans=''.join(res)
        return ans
        