function solution(arr, delete_list) {
    let ans = [];
    for (let i=0; i<arr.length; i++) {
        if (delete_list.includes(arr[i])) {
            continue
        } else {
            ans.push(arr[i])
        }
    }
    return ans;
}