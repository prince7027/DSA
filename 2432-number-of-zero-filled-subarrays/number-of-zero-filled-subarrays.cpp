class Solution {
    long long possible_subarrays(int n){
        return n*(n+1)/2;
    }
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long ans=0;
        long long n=0;
        for(auto& i:nums){
            if(!i) n++;
            else{
                ans+=n*(n+1)/2;
                n=0;
            }
        }
        ans+=n*(n+1)/2;
        return ans;
    }
};