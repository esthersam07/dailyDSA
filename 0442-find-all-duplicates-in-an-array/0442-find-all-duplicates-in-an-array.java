class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        Map<Integer,Integer> m = new HashMap<>();
        ArrayList<Integer> res = new ArrayList<>();
        for(int i:nums){
            if(m.containsKey(i)){
                res.add(i);
            }
            else{
                m.put(i,1);
            }
        }
        return res;
    }
}