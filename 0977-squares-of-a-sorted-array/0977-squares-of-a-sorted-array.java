class Solution {
    public int[] sortedSquares(int[] nums) {
        int n=nums.length;
        int l=0;
        int r=n-1;
        int i=n-1;
        int[] res = new int[n];
        while(l<=r){
            if (Math.abs(nums[l])>Math.abs(nums[r])){
                res[i--]=nums[l]*nums[l];
                l+=1;
            }
            else{
                res[i--]=nums[r]*nums[r];
                r-=1;
            }
        }
        return res;
    }
}