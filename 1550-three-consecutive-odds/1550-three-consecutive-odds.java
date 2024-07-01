class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int res = 0;
        for(int i:arr){
            if(i%2!=0){
                res += 1;
                if(res==3){
                    return true;
                }
            }else{
                res = 0;
            }
        }
        return false;
    }
}