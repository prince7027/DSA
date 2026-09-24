class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        int i = 0;

        for (int &a : nums) {
            int x = a;
            int sum = 0;

            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }

            if (i++ == sum)
                return i - 1;
        }

        return -1;
    }
};