class Solution {
    public int solution(int[] num_list) {
        int ans = 0;
        int multi = 1;
        int sum = 0;
        
        for (int i:num_list) {
            sum += i;
            multi *= i;
        }
        if (multi < (sum*sum)) {
            ans = 1;
        }
        
        return ans;
    }
}