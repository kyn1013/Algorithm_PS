#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {
	int a,c;
	int b[24] = {}; //0~23번
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d", &c);
		b[c]++;
	}
	for (int i = 1; i <= 23; i++) {
		printf("%d ", b[i]);
	}
}
