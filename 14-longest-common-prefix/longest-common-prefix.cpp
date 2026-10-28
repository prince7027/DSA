class Solution {
    struct Node{
        char data;
        Node* child[26];
        int count;
        bool is_terminate;

        Node(char c) {
            data=c;
            for(int i=0;i<26;i++) child[i]=nullptr;
            count=0;
            is_terminate=0;
        }
    };
void insert(Node* root,string s){
    if(!s.size()){
        root->is_terminate=1;
        return;
    }

    int i=s[0]-'a';
    Node* child;

    if(!root->child[i]){
        child=new Node(s[0]);
        root->child[i]=child;
        root->count+=1;
    }
    else child=root->child[i];

    insert(child,s.substr(1));
}
void print(Node* root,string &s){
    s+=root->data;
    if(root->count>1 || root->is_terminate) return;
    for(int i=0;i<26;i++) if(root->child[i]) print(root->child[i],s);
}
public:
    string longestCommonPrefix(vector<string>& strs) {
        Node* root=new Node('\0');
        for(int i=0;i<strs.size();i++){
            insert(root,strs[i]);
        }
        string ans="";
        print(root,ans);
        return ans.substr(1);
    }
};