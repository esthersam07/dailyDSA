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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root==null){
            TreeNode n = new TreeNode(val);
            return n;
        }
        TreeNode cur = root;
        while(cur!=null){
            if(val>cur.val){
                if(cur.right==null){
                    TreeNode n = new TreeNode(val);
                    cur.right = n;
                    return root;
                }
                cur = cur.right;
            }
            else{
                if(cur.left==null){
                    TreeNode n = new TreeNode(val);
                    cur.left = n;
                    return root;
                }
                cur = cur.left;
            }
        }
        return root;
    }
}