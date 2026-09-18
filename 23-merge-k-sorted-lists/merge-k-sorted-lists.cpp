/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        priority_queue<pair<int,ListNode*>>x;
        for(auto i=0;i<lists.size();i++){
            ListNode* temp=lists[i];
            while(temp){
                x.push({temp->val,temp});
                temp=temp->next;
            }
        }
        if(x.empty()) return nullptr;
        ListNode* head=x.top().second;
        x.pop();
        while(!x.empty()){
            ListNode* temp=x.top().second;
            x.pop();
            temp->next=head;
            head=temp;
        }
        return head;
    }
};