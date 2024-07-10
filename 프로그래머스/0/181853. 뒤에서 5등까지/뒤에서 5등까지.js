function solution(num_list) {
    num_list.sort(function(a, b) {
        return a-b   
    });
    return num_list.splice(0, 5)
}