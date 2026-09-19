class TrieNode{
    public:
    char data;
    TrieNode* child[26];
    bool isTerminal;

    //component
    TrieNode(int n){
        data=n;
        for(int i=0;i<26;i++) child[i]=nullptr;
        isTerminal=0;
    }
};
class Trie {
public:
    Trie() {
        
    }
    TrieNode* root=new TrieNode('\0');
    void insert(string word) {
        insert_word(root,word);
    }
    
    void insert_word(TrieNode* root,string s) {
        if(!s.size()) {
            root->isTerminal=1;
            return;
        }
        int i=s[0]-'a';
        if(!root->child[i]){
            root->child[i]=new TrieNode(s[0]);
        }
        insert_word(root->child[i],s.substr(1));
    }
    
    bool search(string word) {
        return search_word(root,word);
    }
    bool search_word(TrieNode* root,string s) {
        if(!s.size())
            return root->isTerminal;
        int i=s[0]-'a';
        if(root->child[i]) return search_word(root->child[i],s.substr(1));
        else return 0;
    }

    bool search_preffix(TrieNode* root,string s) {
        if(!s.size()) return 1;
        int i=s[0]-'a';
        if(root->child[i]) return search_preffix(root->child[i],s.substr(1));
        else return 0;
    }

    bool startsWith(string prefix) {
        return search_preffix(root,prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */