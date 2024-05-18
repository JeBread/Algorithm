function solution(n) {
  const newN = n + "";
  const newArr = newN
    .split("")
    .sort()
    .reverse()
    .join("");

  return +newArr;
}

// 다른 사람 풀이
// function solution(n) {
//     return parseInt((n + '').split('').sort((a, b) => b - a).join(""));
// }
