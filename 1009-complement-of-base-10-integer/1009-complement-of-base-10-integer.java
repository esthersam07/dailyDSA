class Solution {
    public int bitwiseComplement(int n) {
        if(n==0){
            return 1;
        }
        int res = 0;
        int i = 0;
        while(n!=0){
            if((n&1)==0){
                res += 1<<i;
            }
            i+=1;
            n>>=1;
        }
        return res;
        
    }
}