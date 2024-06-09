class Solution {
    public int[] solution(int n, int k) {
        int end = n / k;
        int[] ans = new int[end];
        
        for (int i = 1; i <= end; i++) {
            ans[i-1] = k * i;
        }
        return ans;
    }
}