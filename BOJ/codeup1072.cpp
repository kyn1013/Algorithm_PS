#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {
	int a,b;
	cin >> a;

loop:
	if (a-- != 0) {
		cin >> b;
		cout << b << endl;
		goto loop;
	}

	
	}
