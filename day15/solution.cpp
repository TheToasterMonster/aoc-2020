#include <bits/stdc++.h>
using namespace std;

#define nl '\n'
#define MOD ((int)1e9 + 7)

typedef long long ll;

#define SIZE 6

int input[SIZE] = { 1, 20, 8, 12, 0, 14 };

void solve(int goal) {
    vector<int> turns(input, input + SIZE);
    unordered_map<int, int> last;
    for (int i = 0; i < turns.size() - 1; i++) {
        last[turns[i]] = i;
    }
    for (int i = turns.size(); i < goal; i++) {
        int next;
        if (last.count(turns.back())) {
            next = i - 1 - last[turns.back()];
        } else {
            next = 0;
        }
        last[turns.back()] = i - 1;
        turns.push_back(next);
    }
    cout << turns.back() << nl;
}

int main() {
    cout << "Part 1: ";
    solve(2020);
    cout << "Part 2: ";
    solve(30000000);
}
