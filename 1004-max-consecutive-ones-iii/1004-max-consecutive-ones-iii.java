class Solution {
    public int longestOnes(int[] nums, int k) {
        //sliding window
        //tc - O(n)
        int res = 0;
        int l = 0;
        int r = 0;
        int z = 0;
        while(r<nums.length){
            if(nums[r]==0){
                z+=1;
            }
            if(z>k){
                if(nums[l]==0){
                    z-=1;
                }
                l+=1;
            }
            if(z<=k){
                int temp = r-l+1;
                res = Math.max(res,temp);
            }
            r+=1;
        }
        return res;
    }
}