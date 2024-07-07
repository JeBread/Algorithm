function solution(num_list, n) {
    let ans = 0;
    if (num_list.includes(n)) {
        ans = 1;
    }
    return ans;
}