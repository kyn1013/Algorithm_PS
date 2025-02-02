class Solution {
    public long solution(long n) {
        long answer = 0;

        for (long i = 1; i < 50000000; i++){
            if (n / i == i && n % i == 0){
                return (i+1) * (i+1);
            }
        }
        return -1;
    }
}
