class Solution {
    public int minOperations(int[] nums, int k) {
        int xor=0;
        for(int i:nums){
            xor^=i;
        }
        int diff = xor^k;
        int res = 0;
        while(diff>0){
            diff = diff&(diff-1);
            res+=1;
        }
        return res;
    }
}