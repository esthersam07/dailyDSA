class Solution {
    public int findDuplicate(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        for(int i:nums){
            if(m.containsKey(i)){
                return i;
            }
            m.put(i,1);
        }
        return 0;
    }
}