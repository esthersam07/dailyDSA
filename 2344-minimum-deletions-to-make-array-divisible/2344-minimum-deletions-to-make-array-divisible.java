class Solution {
    public int gcd(int a, int b){
        while(b!=0){
            int temp = a%b;
            a = b;
            b = temp;
        }
        return a;
    }
    public int findgcd(int[] arr){
        int res = arr[0];
        int a = arr[0];
        for(int i = 1;i<arr.length;i++){
            int b = arr[i];
            res = gcd(a,b);
            a = res;
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