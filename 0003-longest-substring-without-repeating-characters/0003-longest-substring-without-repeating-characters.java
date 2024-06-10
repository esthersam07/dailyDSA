class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        Set<Character> charSet = new HashSet<>();
        int l = 0;
        for(int r = 0;r<s.length();r++){
            if(!charSet.contains(s.charAt(r))){
                charSet.add(s.charAt(r));
                res = Math.max(res,r-l+1);
            }
            else{
                while(charSet.contains(s.charAt(r))){
                    charSet.remove(s.charAt(l));
                    l++;
                }
                charSet.add(s.charAt(r));
            }
        }
        return res;
    }
}