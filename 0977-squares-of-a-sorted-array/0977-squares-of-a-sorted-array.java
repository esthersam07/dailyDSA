class Solution {
    public int[] sortedSquares(int[] nums) {
        int l=0;
        int r=nums.length-1;
        ArrayList<Integer> temp = new ArrayList<>();
        while(l<=r){
            if (Math.pow(nums[l],2)>Math.pow(nums[r],2)){
                temp.add((int)Math.pow(nums[l],2));
                l+=1;
            }
            else{
                temp.add((int)Math.pow(nums[r],2));
                r-=1;
            }
        }
        int[] res = new int[temp.size()];
        for (int i = temp.size() - 1; i >= 0; i--) {
            res[temp.size() - 1 - i] = temp.get(i);
        }
        return res;
    }
}