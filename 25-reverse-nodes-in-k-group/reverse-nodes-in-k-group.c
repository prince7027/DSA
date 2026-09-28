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
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode* result;
        int h=1,k1=k;
    
        while(head){
            k1=k;
            struct ListNode* temp=head;
            while(--k1 && head->next)
                head=head->next;

            struct ListNode* temp_1=head->next;
            head->next=NULL;
            
            if(h){
                result=reverse(NULL,temp,temp->next);
                h=0;
            }
            else{
                struct ListNode* temp_2=result;
                
                while(temp_2->next)
                    temp_2=temp_2->next;

                if(k1 && !head->next)
                    temp_2->next=temp;
                else
                    temp_2->next=reverse(NULL,temp,temp->next);
            }
            head=temp_1;
        }
        return result; 
}