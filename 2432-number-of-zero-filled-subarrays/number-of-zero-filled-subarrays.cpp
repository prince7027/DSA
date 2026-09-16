class Solution {
    long long possible_subarrays(long long n){
        return n*(n+1)/2;
    }
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long ans=0;
        int max=0;
        for(auto& i:nums){
            if(!i) max++;
            else{
                ans+=possible_subarrays(max);
                max=0;
            }
        }
        ans+=possible_subarrays(max);
        return ans;
    }
};