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
    public int diameterOfBinaryTree(TreeNode root) {
        int[] d = new int[1];
        func(root,d);
        return d[0];
    }
    public int func(TreeNode root,int[] d){
        if(root==null){
            return 0;
        }
        int lh = func(root.left,d);
        int rh = func(root.right,d);
        d[0] = Math.max(d[0],lh+rh);
        
        return Math.max(lh,rh) + 1;
    }
}