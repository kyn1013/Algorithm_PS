#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {
	long long a, b, c, d, count, sum;
	scanf("%lld %lld %lld %lld", &a, &b, &c, &d);

	for (count = 1, sum = a;; count++, sum = sum * b + c) {
		if (count == d) break;
	}
	printf("%lld", sum);
}
