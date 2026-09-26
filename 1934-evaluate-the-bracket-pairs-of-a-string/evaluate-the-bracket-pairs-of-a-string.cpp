class Solution {
public:
    string evaluate(string s, vector<vector<string>>& know) {
        int n=s.size();
        string ans="";
        unordered_map<string,string>x;

        for(int i=0;i<know.size();i++)
            x[know[i][0]]=know[i][1];
        
        bool a=0;
        string temp;
        for(int i=0;i<n;i++){
            if(s[i]=='('){
                a=1;
                temp="";
                continue;
            }
            if(s[i]==')'){
                a=0;
                if(x[temp]!="") ans+=x[temp];
                else ans+="?";
                continue;
            }

            if(!a)
                ans+=s[i];
            else 
                temp+=s[i];
        }
        return ans;
    }
};