class Solution {
public:
    bool isValid(string se) {
        stack<char>s;
        for(char x:se){
            if(x=='('||x=='{'||x=='['){
                s.push(x);
            }
            else{
                if(s.empty()||(x==')'&s.top()!='(')||(x=='}'&s.top()!='{')||(x==']'&s.top()!='[')){
                    return 0;
                }
                s.pop();
            }
        }
        return s.empty();
    }
};