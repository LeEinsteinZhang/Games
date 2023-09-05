class Connect:
    WINLENGTH = 4
    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.current_player = 1
        self.board = [0] * self.WIDTH * self.HEIGHT

    def get_player(self, col, row):
        pos = col + row * self.WIDTH
        return self.board[pos]

    def set_player(self, col, row):
        pos = col + row * self.WIDTH
        self.board[pos] = self.current_player

    def drop_piece(self, col):
        current_player = self.current_player
        next_player = 0
        if (current_player == 1):
            next_player = 2
        if (current_player == 2):
            next_player = 1
        top_item = self.get_player(col, 0)
        if (top_item != 0):
            return False
        else:
            for j in range(self.HEIGHT - 1, -1, -1):
                current_player = self.get_player(col, j)
                if (current_player == 0):
                    self.set_player(col, j)
                    self.current_player = next_player
                    return True
            return False

    def winner(self):
        # row checktwo mo
        for i in range(self.HEIGHT):
            row_count = 1
            row_item = self.get_player(0, i)
            for j in range(1, self.WIDTH):
                current_item = self.get_player(j, i)
                if current_item == row_item:
                    row_count += 1
                    if row_count == self.WINLENGTH and row_item != 0:
                        return row_item
                else:
                    row_count = 1
                    row_item = current_item
        # col check
        for j in range(self.WIDTH):
            col_count = 1
            col_item = self.get_player(j, 0)
            for i in range(1, self.HEIGHT):
                current_item = self.get_player(j, i)
                if current_item == col_item:
                    col_count += 1
                    if col_count == self.WINLENGTH and col_item != 0:
                        return col_item
                else:
                    col_count = 1
                    col_item = current_item
        # dig check
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                up_dig_count = 1
                up_dig = self.get_player(j, i)
                dn_dig_count = 1
                dn_dig = self.get_player(j, i)
                for k in range(1, self.WINLENGTH):
                    # up
                    if i - k >= 0 and j + k < self.WIDTH:
                        current_item = self.get_player(j + k, i - k)
                        if current_item == up_dig:
                            up_dig_count += 1
                            if up_dig_count == self.WINLENGTH and up_dig != 0:
                                return up_dig
                        else:
                            up_dig_count = 1
                            up_dig = current_item
                    # down
                    if i + k < self.HEIGHT and j + k < self.WIDTH:
                        current_item = self.get_player(j + k, i + k)
                        if current_item == dn_dig:
                            dn_dig_count += 1
                            if dn_dig_count == self.WINLENGTH and dn_dig != 0:
                                return dn_dig
                        else:
                            dn_dig_count = 1
                            dn_dig = current_item
        return 0

    def is_finish(self):
        if (self.winner() != 0):
            return True
        top_count = 0
        for j in range(0, self.WIDTH):
            top_item = self.get_player(j, 0)
            if (top_item != 0):
                top_count += 1
        if (top_count == self.WIDTH):
            return True
        else:
            return  False
