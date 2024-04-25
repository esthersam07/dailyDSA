class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()==0){
            return true;
        }
        int i = 0;
        int j = 0;
        while(i<s.length()){
            if(j>=t.length()){
                return false;
            }
            if(s.charAt(i)==t.charAt(j)){
                i+=1;
                j+=1;
            }
            else{
                j+=1;
            }
        }
        if(i>=s.length()){
            return true;
        }
        return false;
    }
}