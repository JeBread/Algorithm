function solution(str1, str2) {
    let ans = 0;
    if (str2.includes(str1)) {
        ans = 1;
    }
    return ans;
}