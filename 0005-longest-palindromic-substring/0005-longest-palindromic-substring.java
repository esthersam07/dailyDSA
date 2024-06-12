class Solution {
    public String longestPalindrome(String s) {
        int length = 0;
        String res = "";
        for(int i = 0;i<s.length();i++){
            //odd
            int l = i;
            int r = i;
            while(l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
                if(r-l+1>length){
                    res = s.substring(l,r+1);
                    length = r-l+1;
                }
                l--;
                r++;
            }
            //even
            int el = i;
            int er = i+1;
            while(el>=0 && er<s.length() && s.charAt(el)==s.charAt(er)){
                if(er-el+1>length){
                    res = s.substring(el,er+1);
                    length = er-el+1;
                }
                el--;
                er++;
            }
        }
        return res;
    }
}