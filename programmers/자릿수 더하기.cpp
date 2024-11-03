#include <iostream>
#include <string>

using namespace std;

int solution(int n)
{
    int answer = 0;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        answer += str[i] - '0'; //문자를 숫자로 변경, 아스키코드 값만큼 빼줌
    }
    
    return answer;
}
