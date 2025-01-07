import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        
        for (int a : arr){
            if (a % divisor == 0){
                arrList.add(a);
            }
        }
        
        Collections.sort(arrList);
        
        if(arrList.size() == 0){
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[arrList.size()];
        
        for (int i = 0; i < arrList.size(); i++){
            answer[i] = arrList.get(i);
        }
        return answer;
    }
}
