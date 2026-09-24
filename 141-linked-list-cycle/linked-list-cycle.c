/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(!head) return 0;
    struct ListNode *slow=head;
    struct ListNode *fast=head->next;

    while(fast && fast->next){
        if(slow==fast) return 1;
        slow=slow->next;
        fast=fast->next->next;
    }
    return 0;

}