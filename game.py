from random import shuffle


class Cell:
    def __init__(self):
        self.__value = TicTacToe.FREE_CELL

    def __bool__(self):
        if self.__value == 0:
            return True
        return False

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return self.__str__()


class TicTacToe:
    FREE_CELL = 0      
    HUMAN_X = 1        # X
    COMPUTER_O = 2     # 0

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_computer_win
        self.is_draw
        self.is_human_win

    def show(self):
        for i in self.pole:
            print(*i)
        print('_'* 10)

    def human_go(self):
        cells = self.__get_empty_cells()
        cell = tuple(map(int, input('Choose the cell ').split(',')))
        while cell not in cells:
            cell = tuple(map(int, input('Choose the cell ').split(',')))
        self.pole[cell[0]][cell[1]].value = self.HUMAN_X

    def computer_go(self):
        cells = self.__get_empty_cells()
        shuffle(cells)
        self.pole[cells[0][0]][cells[0][1]].value = self.COMPUTER_O

    def __get_empty_cells(self):
        return [(i, j) for i in range(len(self.pole)) for j in range(len(self.pole[i])) if self.pole[i][j].value == 0]

    def __check_win(self, val):
        for i in self.pole:
            if len(list(filter(lambda x: x.value == val, i))) == 3:
                return True
        cells_trans = list(zip(*self.pole))
        for i in cells_trans:
            if len(list(filter(lambda x: x.value == val, i))) == 3:
                return True
        ldiag = [self[0, 0], self[1, 1], self[2, 2]]
        if len(list(filter(lambda x: x == val, ldiag))) == 3:
            return True
        rdiag = [self[0, 2], self[1, 1], self[2, 0]]
        if len(list(filter(lambda x: x == val, rdiag))) == 3:
            return True
        return False

    @property
    def is_human_win(self):
        return self.__check_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.__check_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        if not self.is_computer_win and not self.is_human_win and len(self.__get_empty_cells()) == 0:
            return True
        return False

    def __check_indx(self, indx):
        r, c = indx
        if isinstance(r, int) and isinstance(c, int):
            if 0 <= r <= 2 and 0 <= c <= 2:
                return
        raise IndexError('Wrong index')

    def __getitem__(self, indx):
        self.__check_indx(indx)
        r, c = indx
        return self.pole[r][c].value

    def __setitem__(self, key, val):
        if bool(self):
            self.__check_indx(key)
            r, c = key
            self.pole[r][c].value = val

    def __bool__(self):
        if len(self.__get_empty_cells()) == 0:
            return False
        if self.is_human_win or self.is_computer_win or self.is_draw:
            return False
        return True


if __name__ == '__main__':
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Congrats, you win")
    elif game.is_computer_win:
        print("Try harder and you'll win.")
    else:
        print("Draw.")
