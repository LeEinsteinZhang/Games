// this is the version of text display produced by c++
#include <iostream>
#include <string>
#include <limits>
#include <vector>
using namespace std;


static const int max_row = 7;
static const int max_col = 6;

bool if_win(vector<vector<char>> board, int x, int y, char color) {
    int xnum = 1;
    int ynum = 1;
    int xynum = 1;
    int yxnum = 1;
    bool xu = true;
    bool xd = true;
    bool yu = true;
    bool yd = true;
    bool xyu = true;
    bool xyd = true;
    bool yxu = true;
    bool yxd = true;
    for (int i = 1; i < 4; ++i) {
        if ((x + i < max_row) && board[x + i][y] == color && xu) {
            xnum += 1;
        } else {
            xu = false;
        }
        if ((x - i >= 0) && board[x - i][y] == color && xd) {
            xnum += 1;
        } else {
            xd = false;
        }
        if ((y + i < max_col) && board[x][y + i] == color && yu) {
            ynum += 1;
        } else {
            yu = false;
        }
        if ((y - i >= 0) && board[x][y - i] == color && yd) {
            ynum += 1;
        } else {
            yd = false;
        }
        if ((y + i < max_col && x + i < max_row) && board[x + i][y + i] == color && xyu) {
            xynum += 1;
        } else {
            xyu = false;
        }
        if ((y - i >= 0 && x - i >= 0) && board[x - i][y - i] == color && xyd) {
            xynum += 1;
        } else {
            xyd = false;
        }
        if ((y - i >= 0 && x + i < max_row) && board[x + i][y - i] == color && yxu) {
            yxnum += 1;
        } else {
            yxu = false;
        }
        if ((y + i < max_col && x - i >= 0) && board[x - i][y + i] == color && xyd) {
            xynum += 1;
        } else {
            xyd = false;
        }
        if (xnum == 4 || ynum == 4 || xynum == 4 || yxnum == 4) {
            return true;
        }
    }
    return false;
}

int drop(vector<vector<char>>& board, int x, int y, char color) {
    if (x >= 0 && x < max_row && y >= 0 && y < max_col) {
        board[x][y] = color;
        if (if_win(board, x, y, color)) {
            return 2;
        }
        return 0;
    }  else {
        return 1;
    }
}

void print(vector<vector<char>> board) {
    for (int i = 0; i < max_row; ++i) {
        for (int j = 0; j < max_col; ++j) {
            cout << board[i][j];
        }
        cout << endl;
    }
}

int change_X(vector<vector<char>> board, int y) {
    int x;
    for (int i = 0; i < max_row; ++i) {
        if (board[i][y] != '-') {
            x = i - 1;
            return x;
        }
    }
    x = max_row - 1;
    return x;
}

int main() {
    vector<vector<char>> board(max_row, vector<char>(max_col, '-'));
    char color = 'B';
        for (int i = 0; i < 42; ++i) {
            int y;
            color = i % 2 ? 'W' : 'B';
            while(!(std::cin >> y)) {
                std::cout << "Invalid input. Please enter one integers: " << endl;
                std::cin.clear(); // Clear the error flags
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Remove invalid input
            }
            int x = change_X(board, y);
            int result = drop(board, x, y, color);
            print(board);
            if (result == 1) {
                cout << "please give a valid position" << endl;
                i -= 1;
            } else if (result == 2) {
                cout << "color" << color << "win" << endl;
                return 0;
            }
        }
}
