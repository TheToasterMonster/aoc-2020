#include <bits/stdc++.h>
using namespace std;

#define nl '\n'
#define MOD ((int)1e9 + 7)

typedef long long ll;

const string fp = "./input.txt";
vector<string> lines;
void read() {
    fstream file(fp);
    while (!file.eof()) {
        string s;
        getline(file, s);
        if (s.size() == 0) continue;

        cout << s.size() << " " << s << nl;
    }
    file.close();
}

string lex(const string& s) {
    string res = "";
    for (char c : s) {
        if (c != ' ') {
            res += c;
        }
    }
    return res;
}

ll evaluate(const string& s) {
    stack<ll> nums;
    stack<char> ops;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            nums.push(s[i]);
        } else if (s[i] == '+' || s[i] == '*') {
            
        }
    }
}

int main() {
    cout << "Part 1: ";
    read();
    cout << "Part 2: ";
}
