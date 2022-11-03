#include <bits/stdc++.h>
using namespace std;

#define nl '\n'
#define MOD ((int)1e9 + 7)

typedef long long ll;

const int sz = 8;
const int cycles = 6;
const int zero = cycles;
using Line = vector<char>;
using Plane = vector<Line>;
using Space = vector<Plane>;
Space grid(sz+2*cycles, Plane(sz+2*cycles, Line(2*cycles+1, '.')));
Space tmp(grid);

const string fp = "./input.txt";
void read() {
    fstream file(fp);
    int row = 0;
    while (!file.eof()) {
        string s;
        file >> s;
        for (int i = 0; i < s.size(); i++) {
            grid[zero + row][zero + i][zero] = s[i];
        }
        row++;
    }
    file.close();
}

void simulate() {
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            for (int k = 0; k < grid[0][0].size(); k++) {
                int count = -(grid[i][j][k] == '#');
                for (int di = -1; di <= 1; di++) {
                    if (i + di < 0 || i + di >= grid.size()) continue;
                    for (int dj = -1; dj <= 1; dj++) {
                        if (j + dj < 0 || j + dj >= grid[0].size()) continue;
                        for (int dk = -1; dk <= 1; dk++) {
                            if (k + dk < 0 || k + dk >= grid[0][0].size()) continue;
                            count += (grid[i+di][j+dj][k+dk] == '#');
                        }
                    }
                }
                if (grid[i][j][k] == '#') {
                    if (count == 2 || count == 3) {
                        tmp[i][j][k] = '#';
                    } else {
                        tmp[i][j][k] = '.';
                    }
                } else {
                    if (count == 3) {
                        tmp[i][j][k] = '#';
                    } else {
                        tmp[i][j][k] = '.';
                    }
                }
            }
        }
    }
    swap(grid, tmp);
}

using SpaceTime = vector<Space>;
SpaceTime grid1(sz+2*cycles, Space(sz+2*cycles, Plane(2*cycles+1, Line(2*cycles+1, '.'))));
SpaceTime tmp1(grid1);

void read1() {
    fstream file(fp);
    int row = 0;
    while (!file.eof()) {
        string s;
        file >> s;
        for (int i = 0; i < s.size(); i++) {
            grid1[zero + row][zero + i][zero][zero] = s[i];
        }
        row++;
    }
    file.close();
}

void simulate1() {
    for (int i = 0; i < grid1.size(); i++) {
        for (int j = 0; j < grid1[0].size(); j++) {
            for (int k = 0; k < grid1[0][0].size(); k++) {
                for (int l = 0; l < grid1[0][0][0].size(); l++) {
                    int count = -(grid1[i][j][k][l] == '#');
                    for (int di = -1; di <= 1; di++)
                    {
                        if (i + di < 0 || i + di >= grid1.size())
                            continue;
                        for (int dj = -1; dj <= 1; dj++)
                        {
                            if (j + dj < 0 || j + dj >= grid1[0].size())
                                continue;
                            for (int dk = -1; dk <= 1; dk++)
                            {
                                if (k + dk < 0 || k + dk >= grid1[0][0].size())
                                    continue;
                                for (int dl = -1; dl <= 1; dl++) {
                                    if (l + dl < 0 || l + dl >= grid1[0][0][0].size())
                                        continue;
                                    count += (grid1[i + di][j + dj][k + dk][l + dl] == '#');
                                }
                            }
                        }
                    }
                    if (grid1[i][j][k][l] == '#')
                    {
                        if (count == 2 || count == 3)
                        {
                            tmp1[i][j][k][l] = '#';
                        }
                        else
                        {
                            tmp1[i][j][k][l] = '.';
                        }
                    }
                    else
                    {
                        if (count == 3)
                        {
                            tmp1[i][j][k][l] = '#';
                        }
                        else
                        {
                            tmp1[i][j][k][l] = '.';
                        }
                    }
                }
            }
        }
    }
    swap(grid1, tmp1);
}

int main() {
    cout << "Part 1: ";
    read();
    for (int i = 0; i < 6; i++) {
        simulate();
    }
    int count = 0;
    for (auto& plane : grid) {
        for (auto& row : plane) {
            for (auto& sq : row) {
                count += (sq == '#');
            }
        }
    }
    cout << count << nl;

    cout << "Part 2: ";
    read1();
    for (int i = 0; i < 6; i++) {
        simulate1();
    }
    int count1 = 0;
    for (auto& space : grid1) {
        for (auto& plane : space) {
            for (auto& row : plane) {
                for (auto& sq : row) {
                    count1 += (sq == '#');
                }
            }
        }
    }
    cout << count1 << nl;
}
