/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void func(TreeNode root, int l,List<Integer> res){
        if(root==null){
            return;
        }if(l==res.size()){
            res.add(root.val);
        }
        func(root.right,l+1,res);
        func(root.left,l+1,res);
    } 
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        func(root,0,res);
        return res;
    }
}