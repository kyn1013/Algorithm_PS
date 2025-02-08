class Solution {
    public String solution(String phone_number) {
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < phone_number.length(); i++){
            if(i < (phone_number.length() - 4)){
                answer.append("*");
            }else {
                answer.append(phone_number.charAt(i));
            }
        }
        return answer.toString();
    }
}
