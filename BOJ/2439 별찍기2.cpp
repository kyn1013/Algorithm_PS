#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {

	cin.tie(0);
	int a;
	cin >> a;
	int j(0), k(0);

	for (int i = 1; i <= a; i++) {
		
		for (k = a; k > i; k--) {
			printf(" ");
		}

		for (j = 1; j <= i; j++) {
			printf("*");
		}
	
		printf("\n");
	}

}
