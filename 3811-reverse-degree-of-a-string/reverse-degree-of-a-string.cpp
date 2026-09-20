class Solution {
public:
    int reverseDegree(string s) {
        int j=1,ans=0;
        for(char&i:s)
            ans+=(26-(i-'a'))*j++;
        return ans;
    }
};