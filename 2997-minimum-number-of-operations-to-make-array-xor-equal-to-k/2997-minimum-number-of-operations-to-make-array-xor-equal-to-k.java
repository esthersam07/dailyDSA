class Solution {
    public int minOperations(int[] nums, int k) {
        int xor=0;
        for(int i:nums){
            xor^=i;
        }
        int diff = 0;
        while(xor!=0 || k!=0){
            if((xor&1) != (k&1)){
                diff+=1;
            }
            xor>>=1;
            k>>=1;
        }
        return diff;
    }
}