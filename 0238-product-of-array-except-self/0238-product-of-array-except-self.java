class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] res = new int[len];
        int left=1;
        for(int l=0;l<len;l++){
            res[l]=left;
            left*=nums[l];
        }
        int right=1;
        for(int r=len-1;r>=0;r--){
            res[r]*=right;
            right*=nums[r];
        }
        return res;
    }
}