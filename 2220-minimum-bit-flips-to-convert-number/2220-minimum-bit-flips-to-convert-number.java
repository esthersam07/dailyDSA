class Solution {
    public int minBitFlips(int start, int goal) {
        int res=0;
        int c=start^goal;
        while(c>0){
            c=c&(c-1);
            res+=1;
        }
        return res;
    }
}