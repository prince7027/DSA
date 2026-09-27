/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode* prev,struct ListNode* curr,struct ListNode* Next){
    while(Next){
        curr->next=prev;
        prev=curr;
        curr=Next;
        Next=Next->next;
    }
    curr->next=prev;
    return curr;
}
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* temp=head;
    if(head) 
        return reverse(NULL,temp,temp->next);
    return head;
}