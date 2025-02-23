import java.util.ArrayList;
class Solution {
    public Long solution(long n) {
        long answer = 0;
        ArrayList<Long> list = new ArrayList<Long>();
        
        while(n > 0){
            list.add(n % 10);
            n /= 10;
        }
        
        for(int i = 0; i < list.size(); i++){
            for(int j = i + 1; j < list.size(); j++){
                if(list.get(i) < list.get(j)){
                    long temp = list.get(j);
                    list.set(j, list.get(i));
                    list.set(i, temp);
                }
            }
        }
        
        int idx = 1;
        for (int i = list.size() - 1; i >= 0; i--){
            answer = answer + (list.get(i) * idx);
            idx = idx * 10;
        }
        
        
        return answer;
    }
}