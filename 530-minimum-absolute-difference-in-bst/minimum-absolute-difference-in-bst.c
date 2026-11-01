/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void inorder(struct TreeNode* root,int **x){
    if(!root) return;
    inorder(root->left,x);
    **x=root->val;
    (*x)++;
    inorder(root->right,x);
}
int getMinimumDifference(struct TreeNode* root) {
    int* ans = malloc(100000 * sizeof(int));
    int *point=ans;
    inorder(root,&point);

    int min=INT_MAX;
    for(int i=1;i<point - ans;i++){
        int temp=ans[i]-ans[i-1];
        if(temp<min)
            min=temp;
    }
    return min;
}