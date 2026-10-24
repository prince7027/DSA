class LRUCache {
    struct Node{
        int key,data;
        Node *prev,*next;
        Node(int k, int v) : key(k), data(v), prev(nullptr), next(nullptr) {}
    };
    unordered_map<int,Node*>x;
    Node* head=new Node(-1,-1), *tail=new Node(-1,-1);
    int s;
public:
    LRUCache(int capacity) {
        head->next=tail;
        tail->prev=head;
        s=capacity;
    }
    
    int get(int key) {
        if(!x[key]) return -1;

        Node* temp = x[key];

        temp->prev->next=temp->next;
        temp->next->prev=temp->prev;

        temp->next=head->next;
        head->next->prev=temp;
        temp->prev=head;
        head->next=temp;
        return temp->data;
    }
    
    void put(int key, int value) {
        Node* temp;
        if(!x[key]){
            temp=new Node(key,value);
            x[key]=temp;
            if(!s--){
                x[tail->prev->key]=nullptr;
                tail->prev->data=-1;
                tail->prev=tail->prev->prev;
                tail->prev->next=tail;
                s++;
            }
        }
        else{
            temp=x[key];
            temp->data=value;
            temp->prev->next=temp->next;
            temp->next->prev=temp->prev;
        }
        temp->next=head->next;
        head->next->prev=temp;
        temp->prev=head;
        head->next=temp;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */