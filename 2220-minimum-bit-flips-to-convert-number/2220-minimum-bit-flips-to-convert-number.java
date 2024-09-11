class Solution {
    public int minBitFlips(int start, int goal) {
        int c = start ^ goal;
        int res = 0;
        while(c>0){
            if((c & 1)==1){
                res += 1;
            }
            c = c>>1;
        }
        return res;
    }
}