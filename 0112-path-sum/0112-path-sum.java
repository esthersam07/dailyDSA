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
    public boolean func(TreeNode root, int targetSum, int s) {
        if(root==null){
            return false;
        }
        s += root.val;
        if(root.left==null && root.right==null){
            return s==targetSum;
        }
        return func(root.left,targetSum,s)||func(root.right,targetSum,s);
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        int s = 0;
        return func(root,targetSum,s);
    }
}