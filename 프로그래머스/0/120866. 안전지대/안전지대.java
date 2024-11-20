class Solution {
  public int solution(int[][] board) {
    int answer = 0;

    int[][] newBoard = new int[board.length][board[0].length];

    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        if (board[i][j] == 1) {
          markDanger(i, j, newBoard);
        }
      }
    }

    for (int i = 0; i < newBoard.length; i++) {
      for (int j = 0; j < newBoard[i].length; j++) {
        if (newBoard[i][j] == 0) {
          answer++;
        }
      }
    }

    return answer;
  }

  void markDanger(int i, int j, int[][] newBoard) {
    int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
    int[] dy = {1, 1, 1, 0, 0, -1, -1, -1};

    for (int v = 0; v < dx.length; v++) {
      int nx = i + dx[v];
      int ny = j + dy[v];

      if (nx >= 0 && ny >= 0 && nx < newBoard.length && ny < newBoard[0].length) {
        newBoard[nx][ny] = 1;
      }
    }

    newBoard[i][j] = 1;
  }
}