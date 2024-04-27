function solution(n) {
    let nString = n.toString().split("").map(Number)
    let sum = 0;

    for (let i = 0; i < nString.length; i++) {
        sum += nString[i]
    }

    return sum
}