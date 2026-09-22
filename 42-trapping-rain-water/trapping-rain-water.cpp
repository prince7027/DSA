class Solution {
public:
    int trap(vector<int>& h) {
        int ans = 0, current = 0, n = h.size();
        stack<int> s; // Only store indices

        while (current < n) {
            while (!s.empty() && h[current] > h[s.top()]) {
                int top = s.top();
                s.pop();
                if (s.empty()) break;
                
                int distance = current - s.top() - 1;
                int bounded_height = min(h[current], h[s.top()]) - h[top];
                ans += distance * bounded_height;
            }
            s.push(current++);
        }
        return ans;
    }
};