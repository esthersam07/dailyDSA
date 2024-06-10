class Solution {
    //to find gcd of the array
    public int findgcd(int[] arr){
        int res = arr[0];
        for(int i = 1;i<arr.length;i++){
            int b = arr[i];
            while(b!=0){
                int temp = res%b;
                res = b;
                b = temp;
            }
        }
        return res;
    }
    public int minOperations(int[] nums, int[] numsDivide) {
        int gcdArr = findgcd(numsDivide);
        Arrays.sort(nums);
        for(int i = 0;i<nums.length;i++){
            if(gcdArr%nums[i]==0){
                return i;
            }
        }
        return -1;
    }
}