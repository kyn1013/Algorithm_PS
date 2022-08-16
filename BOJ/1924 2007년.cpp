#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int mon, day;
	cin >> mon >> day;
	if (mon == 1) {
		if (day % 7 == 1) cout << "MON";
		else if(day % 7 == 2) cout << "TUE";
		else if (day % 7 == 3) cout << "WED";
		else if (day % 7 == 4) cout << "THU";
		else if (day % 7 == 5) cout << "FRI";
		else if (day % 7 == 6) cout << "SAT";
		else if (day % 7 == 0) cout << "SUN";
	}
	if (mon == 2) {
		if (day % 7 == 5) cout << "MON";
		else if (day % 7 == 6) cout << "TUE";
		else if (day % 7 == 0) cout << "WED";
		else if (day % 7 == 1) cout << "THU";
		else if (day % 7 == 2) cout << "FRI";
		else if (day % 7 == 3) cout << "SAT";
		else if (day % 7 == 4) cout << "SUN";
	}
	if (mon == 3) {
		if (day % 7 == 5) cout << "MON";
		else if (day % 7 == 6) cout << "TUE";
		else if (day % 7 == 0) cout << "WED";
		else if (day % 7 == 1) cout << "THU";
		else if (day % 7 == 2) cout << "FRI";
		else if (day % 7 == 3) cout << "SAT";
		else if (day % 7 == 4) cout << "SUN";
	}
	if (mon == 4) {
		if (day % 7 == 2) cout << "MON";
		else if (day % 7 == 3) cout << "TUE";
		else if (day % 7 == 4) cout << "WED";
		else if (day % 7 == 5) cout << "THU";
		else if (day % 7 == 6) cout << "FRI";
		else if (day % 7 == 0) cout << "SAT";
		else if (day % 7 == 1) cout << "SUN";
	}
	if (mon == 5) {
		if (day % 7 == 0) cout << "MON";
		else if (day % 7 == 1) cout << "TUE";
		else if (day % 7 == 2) cout << "WED";
		else if (day % 7 == 3) cout << "THU";
		else if (day % 7 == 4) cout << "FRI";
		else if (day % 7 == 5) cout << "SAT";
		else if (day % 7 == 6) cout << "SUN";
	}
	if (mon == 6) {
		if (day % 7 == 4) cout << "MON";
		else if (day % 7 == 5) cout << "TUE";
		else if (day % 7 == 6) cout << "WED";
		else if (day % 7 == 0) cout << "THU";
		else if (day % 7 == 1) cout << "FRI";
		else if (day % 7 == 2) cout << "SAT";
		else if (day % 7 == 3) cout << "SUN";
	}
	if (mon == 7) {
		if (day % 7 == 2) cout << "MON";
		else if (day % 7 == 3) cout << "TUE";
		else if (day % 7 == 4) cout << "WED";
		else if (day % 7 == 5) cout << "THU";
		else if (day % 7 == 6) cout << "FRI";
		else if (day % 7 == 0) cout << "SAT";
		else if (day % 7 == 1) cout << "SUN";
	}
	if (mon == 8) {
		if (day % 7 == 6) cout << "MON";
		else if (day % 7 == 0) cout << "TUE";
		else if (day % 7 == 1) cout << "WED";
		else if (day % 7 == 2) cout << "THU";
		else if (day % 7 == 3) cout << "FRI";
		else if (day % 7 == 4) cout << "SAT";
		else if (day % 7 == 5) cout << "SUN";
	}
	if (mon == 9) {
		if (day % 7 == 3) cout << "MON";
		else if (day % 7 == 4) cout << "TUE";
		else if (day % 7 == 5) cout << "WED";
		else if (day % 7 == 6) cout << "THU";
		else if (day % 7 == 0) cout << "FRI";
		else if (day % 7 == 1) cout << "SAT";
		else if (day % 7 == 2) cout << "SUN";
	}
	if (mon == 10) {
		if (day % 7 == 1) cout << "MON";
		else if (day % 7 == 2) cout << "TUE";
		else if (day % 7 == 3) cout << "WED";
		else if (day % 7 == 4) cout << "THU";
		else if (day % 7 == 5) cout << "FRI";
		else if (day % 7 == 6) cout << "SAT";
		else if (day % 7 == 0) cout << "SUN";
	}
	if (mon == 11) {
		if (day % 7 == 5) cout << "MON";
		else if (day % 7 == 6) cout << "TUE";
		else if (day % 7 == 0) cout << "WED";
		else if (day % 7 == 1) cout << "THU";
		else if (day % 7 == 2) cout << "FRI";
		else if (day % 7 == 3) cout << "SAT";
		else if (day % 7 == 4) cout << "SUN";
	}
	if (mon == 12) {
		if (day % 7 == 3) cout << "MON";
		else if (day % 7 == 4) cout << "TUE";
		else if (day % 7 == 5) cout << "WED";
		else if (day % 7 == 6) cout << "THU";
		else if (day % 7 == 0) cout << "FRI";
		else if (day % 7 == 1) cout << "SAT";
		else if (day % 7 == 2) cout << "SUN";
	}
}
