/*
you need to parenthesize i think. 
( ...% )   != 0
might be old C++ ? 
  I know Python is old python
  */

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Utility function to check if there is a repetition number in the given matrix ranges.
bool sudokuUtility(const vector<vector<char>>& board, int rowStart, int rowEnd, int colStart, int colEnd) {
  int size = board.size();
  vector<bool> numExists(size, false);
  
  for (int i = rowStart; i <= rowEnd; ++i) {
    for (int j = colStart; j <= colEnd; ++j) {
      int cur = board[i][j] - 1;
      if (numExists[cur]) return false;
      numExists[cur] = true;
    }
  }
  
  return true;
}

bool sudokuSolve( const vector<vector<char>>& board ) 
{
  int size = board.size();
  //if (size % std::sqrt(size) != 0) return false;

  // Check for every row
  for (int i = 0; i < size; ++i) {
    if ( !sudokuUtility(board, i, i, 0, size - 1) ) return false;
  }
  
  // Check for every col
  for (int i = 0; i < size; ++i) {
    if ( !sudokuUtility(board, 0, size - 1, i, i) ) return false;
  }
  
  int root = std::sqrt(size);
  for (int i = 0; i < root; ++i) {
    for (int j = 0; j < root; ++j) {
      
      int rowStart = i * root;
      int rowEnd = i * root + (root - 1);
      int colStart = j * root ;
      int colEnd = j * root + (root - 1);
      if ( !sudokuUtility(board, rowStart, rowEnd, colStart, colEnd) ) return false;
    }
  }
  
  return true;
}

/*
might be old C++ ? 
  I know Python is old python
  */
int main() {
  
  vector<vect
  return 0;
}
