/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        //base case
        if(!root) return root;

        //main logic: using bfs/level order traversal

        queue<Node*>q;
        q.push(root);
        
        while(!q.empty()){
            Node* prev=nullptr;
            int s = q.size();
            for(int i=0;i<s;i++){
                Node* temp=q.front();
                q.pop();
                if(temp->left){
                    if(prev) prev->next=temp->left;
                    prev=temp->left;
                    q.push(temp->left);
                    
                }
                if(temp->right){
                    if(prev) prev->next=temp->right;
                    prev=temp->right;    
                    q.push(temp->right); 
                }
            }
        }
        return root;
    }
};