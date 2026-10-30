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
    void sum(TreeNode* root, int targetSum,vector<int>temp,vector<vector<int>> &ans){
        if(!root) return;
        
        int a=root->val;
        temp.push_back(a);

        // Check only at leaf nodes
        if (!root->left && !root->right) {
            if (!(targetSum-a)) ans.push_back(temp);
            return;
        }
        sum(root->left,targetSum-a,temp,ans);
        sum(root->right,targetSum-a,temp,ans);
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int>temp;
        vector<vector<int>> ans;

        sum(root,targetSum,temp,ans);
        return ans;
    }
};