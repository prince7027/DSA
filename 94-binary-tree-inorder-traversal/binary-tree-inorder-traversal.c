/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void inorder(struct TreeNode* root,int **x){
    if(!root) return;
    inorder(root->left,x);
    **x=root->val;
    (*x)++;
    inorder(root->right,x);
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* ans = malloc(101 * sizeof(int));
    int *point=ans;
    inorder(root,&point);
    *returnSize = point - ans;
    return ans;
}