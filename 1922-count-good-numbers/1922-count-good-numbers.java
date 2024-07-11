class Solution {
    private long mod = 1_000_000_007;
    public int countGoodNumbers(long n) {
        long e = (n+1)/2;
        long o = n/2;
        long f = pow(5,e)%mod;
        long s = pow(4,o)%mod;
        return (int)((f*s)%mod);
    }
    private long pow(long x, long n){
        if(n==0) return 1;
        long temp = pow(x,n/2);
        if(n%2==0){
            return (temp*temp)%mod;
        }else{
            return (x*temp*temp)%mod;
        }
    }
}
