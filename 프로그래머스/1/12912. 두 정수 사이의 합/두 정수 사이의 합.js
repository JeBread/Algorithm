function solution(a, b) {
    let ans = 0;
    
    for(let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    	ans = ans + i;
    }
    
    return ans;
}