#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    long long answer = 0;
    long long n(num); //오버 플로우가 일어날 수 있기에 타입을 따로 만들어서 지정함
    if(n == 1) return 0;
    for(long long i=1;i<=500;i++){
        if(n % 2 == 0){
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
        
        if(n == 1) return i;
    }
    return -1;
}
