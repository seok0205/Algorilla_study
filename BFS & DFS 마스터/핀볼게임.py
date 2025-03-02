class PinballGame:
    def __init__(self, board, whirlpools):
        self.board = board  # N x N 게임판
        self.whirlpools = whirlpools  # {번호: (x, y), ...}
        self.N = len(board)
        self.dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
        self.dy = [0, 0, -1, 1]
    
    def move(self, x, y, direction):
        score = 0
        start_x, start_y = x, y
        while True:
            x += self.dx[direction]
            y += self.dy[direction]
            
            if not (0 <= x < self.N and 0 <= y < self.N):  # 벽 충돌
                direction = (direction + 2) % 4
                score += 1
                continue
            
            cell = self.board[x][y]
            
            if cell == -1:  # 블랙홀 만나면 종료
                return score
            
            if 6 <= cell <= 10:  # 월풀
                x, y = self.whirlpools[cell] if (x, y) != self.whirlpools[cell] else (x, y)
                continue
            
            if 1 <= cell <= 5:  # 블록 반사 처리
                direction = self.reflect(cell, direction)
                score += 1
                
            if (x, y) == (start_x, start_y):  # 처음 위치로 돌아오면 종료
                return score
    
    def reflect(self, block, direction):
        reflect_map = {
            1: [1, 3, 0, 2],
            2: [3, 0, 1, 2],
            3: [2, 0, 3, 1],
            4: [1, 2, 3, 0],
            5: [1, 0, 3, 2]
        }
        return reflect_map[block][direction]

# 예제 실행
board = [
    [0, 0, 1, 0, 0],
    [0, -1, 0, 6, 0],
    [0, 2, 0, 0, 0],
    [5, 0, 3, 0, 7],
    [0, 0, 4, 0, 0]
]
whirlpools = {6: (3, 4), 7: (1, 3)}

game = PinballGame(board, whirlpools)
score = game.move(2, 2, 3)  # 예제: (2,2)에서 우측으로 시작
print("Score:", score)
