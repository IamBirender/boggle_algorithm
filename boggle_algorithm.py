from collections import defaultdict
class solution:
    def __init__(self, board):
        self.board = board
        self.word = None
        self.board_map = self.convert_to_hash()
        
    def convert_to_hash(self):
        board_map = defaultdict(list)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                board_map[self.board[i][j]].append((i, j))
        return board_map
                
    def boggle_approach(self, word):
        if len(word) == 0:
            return True
        
        self.word = word
        return self.if_exist(0,None, set())
        
    def if_exist(self, idx, prev_idx, seen):
        if idx == len(self.word):
            return True
        
        if self.word[idx] not in self.board_map:
            return False
        
        for curr_idx in self.board_map[self.word[idx]]:
            print(curr_idx, self.word[idx], idx, seen)
            if curr_idx in seen:
                continue
            seen.add(curr_idx)
            if prev_idx == None:
                return self.if_exist(idx+1, curr_idx, seen)
            
            if not self._are_adj(prev_idx, curr_idx) and curr_idx not in seen:
                continue

            return self.if_exist(idx+1, curr_idx, seen)
    
        return False
    
    def _are_adj(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        return abs(x2-x1) <= 1 and abs(y2-y1) <= 1
            
    def does_exist(self, word):
        if len(word) == 0:
            return True
        self.word = word
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == word[0]:
                    if self.dfs_solution(0, i, j, set()):
                        return True
        else:
            return False
    
    def dfs_solution(self, idx, i, j, seen):
        if idx == len(self.word):
            return True
        if 0 <= i < len(self.board) \
            and 0 <= j < len(self.board[0]) \
                and (i, j) not in seen \
                    and self.word[idx] == self.board[i][j]:
                        seen.add((i, j))
                        return self.dfs_solution(idx+1, i+1, j, seen) \
                            or self.dfs_solution(idx+1, i-1, j, seen) \
                                or self.dfs_solution(idx+1, i, j+1, seen)\
                                    or self.dfs_solution(idx+1, i, j-1, seen)
        else:
            return False
        
board = [list("pingu"), list("ringu"), list("tingu"),list("nangu"),list("budhu")]
for b in board: print(b)
word = ["pingu", "budhu","sangu", "iiau"]
obj = solution(board)
obj.convert_to_hash()

for key, value in obj.board_map.items():
    print(key, value)

for w in word:
    # if w == "iiau":
    print(obj.boggle_approach(w))
                            
        
