#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0);
	float arr[1000] = {};
	float score[1000] = {};
	float N,M,average(0);
	scanf("%f", &N);
	for (int i = 0; i < N; i++) scanf("%f",&arr[i]); //점수 받아오기
	M=arr[0];
	for (int i = 0; i < N; i++) {
		if (arr[i] > M) M = arr[i];
	} //최대값 찾기
	for (int i = 0; i < N; i++) {
		score[i] = arr[i] / M * 100;
	}
	for (int i = 0; i < N; i++) {
		average += score[i];
	}

	printf("%.5f", average / N);

}
