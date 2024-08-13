from typing import Any

def check_next(board, current_point):
    cur_r, cur_c = current_point
    next = []
    # 벽에 부딪히는지 확인
    if cur_r-1 > -1 and board[cur_r-1][cur_c] == 0:  # 상
        next.append([cur_r-1, cur_c])
    if cur_r+1 != len(board) and board[cur_r+1][cur_c] == 0:  # 하
        next.append([cur_r+1, cur_c])
    if cur_c-1 > -1 and board[cur_r][cur_c-1] == 0:  # 좌
        next.append([cur_r, cur_c-1])
    if cur_c+1 != len(board) and board[cur_r][cur_c+1] == 0:  # 우
        next.append([cur_r, cur_c+1])
    return next

def solution(board, start, end):
    can_go_list = [start]
    while can_go_list:
        current_point = can_go_list.pop()  # 현재 위치를 갱신
        board[current_point[0]][current_point[1]] = 2 # 이미 방문한 곳(현재 위치)은 표시해주기
        can_go_list.extend(check_next(board, current_point))  # 갈 수 있는 곳 탐색
        if can_go_list[-1] == end:
            return "YES"
    return "NO"

class SAMPLE_1:
    def __init__(self) -> None:
        self.board = [[1,1,1,1,1,0,1],
                [1,0,1,1,0,0,1],
                [1,0,0,1,0,1,1],
                [1,1,0,0,0,1,1],
                [1,1,1,0,1,1,1],
                [0,0,0,0,0,0,0]]
        self.start = [5, 0]
        self.end = [0, 5]
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.board, self.start, self.end

def test_1():
    TEST_SAMPLE = SAMPLE_1()
    if solution(TEST_SAMPLE.board, TEST_SAMPLE.start, TEST_SAMPLE.end) == "YES":
        return "PASS"
    return "FAIL"

print("Test 1: ", test_1())
