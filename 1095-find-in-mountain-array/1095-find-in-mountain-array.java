/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findPeak(MountainArray mountainArr){
        int n = mountainArr.length();
        int l = 0;
        int r = n-1;
        while(l<r){
            int m = (l+r)/2;
            if(mountainArr.get(m)>mountainArr.get(m+1)){
                r = m;
            }else{
                l = m+1;
            }
        }
        return l;
    }
    //function for binary search
    public int binarySearch(MountainArray mountainArr,int l,int r,int target,boolean isAsc){
        while(l<=r){
            int m = (l+r)/2;
            int cur = mountainArr.get(m);
            if(cur==target){
                return m;
            }
            if(isAsc){
                if(cur<target){
                    l = m+1;
                }else{
                    r = m-1;
                }
            }else{
                if(cur<target){
                    r = m-1;
                }else{
                    l = m+1;
                }
            }
        }
        return -1;
    }
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        int peak = findPeak(mountainArr);
        int ans = binarySearch(mountainArr,0,peak,target,true);
        if(ans!=-1){
            return ans;
        }
        return binarySearch(mountainArr,peak+1,n-1,target,false);
    }
}