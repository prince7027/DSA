class Solution {
public:
    int findTheWinner(int n, int k) {
        queue<int>s;
        for(int i=1;i<n+1;i++)
            s.push(i);
        int temp = s.front();
        while(!s.empty()){
            int a=k;
            while(--a){
                temp = s.front();
                s.pop();
                if(s.empty()) return temp;
                else s.push(temp);
            }
            temp = s.front();
            s.pop();
        }
        return temp;
    } 
};