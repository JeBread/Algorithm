function solution(my_string, target) {
    let ans = 0;
    if (my_string.includes(target)) {
        ans = 1;
    }
    return ans;
}