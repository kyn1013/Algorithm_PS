class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long s = 0;
        for (int i = 1; i <= count; i++){
            s += price * i;
        }
        
        if (money - s > 0){
            return 0;
        } else {
            answer = (money - s) * -1;
            return answer;
        }
    }
}
