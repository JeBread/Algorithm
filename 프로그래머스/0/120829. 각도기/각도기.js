function solution(angle) {
    let ans = 0
    if (angle - 90 < 0) {
        ans = 1}
    else if (angle - 90 == 0) {
        ans = 2
    }
    else if (angle - 180 < 0) {
        ans = 3
    }
    else {ans = 4}
    
    return ans;
}