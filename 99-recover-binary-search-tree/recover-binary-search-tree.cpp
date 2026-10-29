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
void inorder(TreeNode* root,vector<TreeNode*>&x){
    if(!root) return;
    inorder(root->left,x);
    x.push_back(root);
    inorder(root->right,x);
}
class Solution {
public:
    void recoverTree(TreeNode* root) {
        vector<TreeNode*>x;
        inorder(root,x);
        TreeNode *p1=nullptr,*p2;

        for(int i=0;i<x.size()-1;i++){
            if(x[i]->val > x[i+1]->val){
                if(!p1) p1=x[i];
                p2=x[i+1];
            }
        }
        swap(p1->val,p2->val);
    }
};