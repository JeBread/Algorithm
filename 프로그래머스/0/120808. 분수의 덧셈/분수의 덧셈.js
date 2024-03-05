function solution(numer1, denom1, numer2, denom2) {
    let ans = [];

    // 분모의 최소공배수를 구하는 함수
    function getLCM(denom1, denom2) {
        let lcm = Math.max(denom1, denom2);
        while(true) {
            if(lcm % denom1 == 0 && lcm % denom2 == 0) {
                break;
            }
            lcm++;
        }
        return lcm;
    }

    // 최소공배수 계산
    let lcm = getLCM(denom1, denom2);

    // 두 분수를 더한 분자 계산
    let sumNumer = numer1 * (lcm / denom1) + numer2 * (lcm / denom2);

    // 분자와 분모의 최대공약수 계산
    function gcd(a, b) {
        return b ? gcd(b, a % b) : a;
    }

    let greatestCommonDivisor = gcd(sumNumer, lcm);

    // 기약분수로 변환하여 결과 반환
    ans.push(sumNumer / greatestCommonDivisor);
    ans.push(lcm / greatestCommonDivisor);

    return ans;
}