class Solution {
    public int addDigits(int num) {
        while(num>9){
            int res = 0;
            while(num!=0){
                int i = num % 10;
                res += i;
                num = num/10;
            }
            num = res;
        }
        return num;
    }
}