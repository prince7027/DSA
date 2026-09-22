/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    void tree(TreeNode* root,int &temp){
        if(!root) return;
        if(temp<root->val) tree(root->left,temp);
        else tree(root->right,temp);
        
        if(temp){
            TreeNode* t1=new TreeNode(temp);
            if(temp<root->val) root->left=t1;
            else root->right=t1;
            temp=0;
        }
    }
public:
    TreeNode* bstFromPreorder(vector<int>& x) {
        int i=0;
        TreeNode* root=new TreeNode(x[0]);
        for(int i=1;i<x.size();i++){
            tree(root,x[i]);
        }
        return root;
    }
};