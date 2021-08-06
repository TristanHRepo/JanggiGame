# Author: Tristan Harville
# Date: 02-27-2021
# Description: A program that runs a basic version of the game Janggi. This program contains a class that is used to
# initiate instances of the game Janggi. The class checks to make sure that each piece that is attempted to move is
# validated to ensure the move is a valid move. The class also checks for checks and checkmates and appropriately labels
# who won that game when the game is finished.

class JanggiGame:
    """This is a Janggi game with methods used to play the game and get the game state. This class will include a method
    that will print the board(print_board), get the current state of the game (get_game_state), check if a player is in
    check (is_in_check), and the ability to make a move (make_move). This class includes methods for each piece that are
    called when the piece is requested to be moved. These methods check to see if the move is valid and if the general
    is in check. This class also includes get methods for various variables initiated in the init method. Finally, this
    class has methods to retrieve the moves a piece can make (get_piece_move), a method to check if a move will result
    in a general being in check (check_checker), and a method to check if a checkmate has occured (is_checkmate)."""

    def __init__(self):
        """Initiates the Janggi game with a fresh board and initial game states. The board is hardcoded. The other
        variables are set to the initial game state and the game is ready to begin with a move by blue first. The move
        will be over when a piece of the correct team is moved. The game_state is unfinished until a general is in
        checkmate. red_check and blue_check tell if general is in check (is True when the general is in check). Palace
        identifies the spaces that are considered a palace for special rules that apply here. Row range and column range
        help when indexing where a move will end up and is used in various methods to evaluate movement."""

        self._player_counter = 'B'
        self._next_player = 'R'
        self._red_check = False
        self._blue_check = False
        self._game_state = 'UNFINISHED'
        self._board = {'a1': 'RCH', 'b1': 'RE', 'c1': 'RH', 'd1': 'RGD', 'e1': ' ', 'f1': 'RGD', 'g1': 'RE', 'h1': 'RH',
                       'i1': 'RCH',
                       'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': 'RGE', 'f2': ' ', 'g2': ' ', 'h2': ' ',
                       'i2': ' ',
                       'a3': ' ', 'b3': 'RCA', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': 'RCA',
                       'i3': ' ',
                       'a4': 'RS', 'b4': ' ', 'c4': 'RS', 'd4': ' ', 'e4': 'RS', 'f4': ' ', 'g4': 'RS', 'h4': ' ',
                       'i4': 'RS',
                       'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
                       'i5': ' ',
                       'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
                       'i6': ' ',
                       'a7': 'BS', 'b7': ' ', 'c7': 'BS', 'd7': ' ', 'e7': 'BS', 'f7': ' ', 'g7': 'BS', 'h7': ' ',
                       'i7': 'BS',
                       'a8': ' ', 'b8': 'BCA', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': 'BCA',
                       'i8': ' ',
                       'a9': ' ', 'b9': ' ', 'c9': ' ', 'd9': ' ', 'e9': 'BGE', 'f9': ' ', 'g9': ' ', 'h9': ' ',
                       'i9': ' ',
                       'a10': 'BCH', 'b10': 'BE', 'c10': 'BH', 'd10': 'BGD', 'e10': ' ', 'f10': 'BGD', 'g10': 'BE',
                       'h10': 'BH', 'i10': 'BCH'
                       }
        self._palace = ['d1', 'd2', 'd3', 'd8', 'd9', 'd10', 'e1', 'e2', 'e3', 'e8', 'e9', 'e10', 'f1', 'f2', 'f3',
                        'f8', 'f9', 'f10']
        self._row_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._column_range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def get_board(self):
        """Returns the board when called. Used in other methods to get the board or to get the value in a key value pair
        from the dictionary containing the board."""
        return self._board

    def get_player_counter(self):
        """Returns the value of the player counter. The player counter tells which players' turn it is. The player
        counter is switched after a successful piece move by that player."""
        return self._player_counter

    def get_next_player(self):
        """Returns the value of the next player variable. The variable keeps up with which players turn is next. This is
        used in some methods for simulated moves when calculating check and checkmate scenarios."""
        return self._next_player

    def get_palace(self):
        """Return the palace spaces list. The palace variables is a list that contains all the keys of the spaces in
        both teams palaces. This is used for calculating special palace movement in various movement methods."""
        return self._palace

    def get_game_state(self):
        """Returns that current state of the game. The state will be changed if a general is in check mate. Otherwise,
        this method will display 'UNFINISHED' until the game is finished."""
        return self._game_state

    def print_board(self):
        """"Prints the board in its current state. Does this by printing out the dictionary in the proper order."""

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        print(" ", end="")
        for column in letters:
            print('| ', end="")
            print(column.upper(), end="")
            print(' ', end="")
        print('')

        for row in numbers:
            if row == '10':
                print(row, end='')
            else:
                print(row+' ', end='')
            for column in letters:
                current_key = column+row
                if len(self.get_board()[current_key]) == 3:
                    print(self.get_board()[current_key] + ' ', end='')
                if len(self.get_board()[current_key]) == 2:
                    print(self.get_board()[current_key] + '  ', end='')
                if len(self.get_board()[current_key]) == 1:
                    print(self.get_board()[current_key] + '   ', end='')
            print('')

    def is_in_check(self, player):
        """Checks if a player is in check. This method will simply return if the general is in check by using the
        initiated variable. After a piece moves the general will be marked as check if the move provokes a check
        scenario."""
        if player == 'red':
            return self._red_check
        else:
            return self._blue_check

    def make_move(self, from_pos, to_pos):
        """Makes a move for the player by checking the piece that is at the first location and making sure that the
        piece can be moved to the position specified. This method will make sure that the piece specified is checked by
        the proper method using the board dictionary. This method also ensures that a valid movement is made and checks
        for if the game is finished, if the space specified is on the board, if the space has a piece ot move,
        if a player is in check, if a player is passing a turn, and finally checks which piece is being moved. When,
        a piece is specified, calls on the appropriate method to check if the move specified is a valid move. The method
        then checks to see if the move causes a player to be in check. If so, then checks to see if checkmate has
        occured."""

        board = self.get_board()

        # if game is over, then moves can not be made
        if self.get_game_state() != 'UNFINISHED':
            return False

        # check if move positions are actually on the board
        if from_pos not in board:
            return False
        if to_pos not in board:
            return False

        # put dictionary values into variables
        from_value = self.get_board()[from_pos]
        to_value = self.get_board()[to_pos]

        # check if from position has a piece
        if from_value == ' ':
            return False

        # check to make sure correct piece is being moved by player
        if self.get_player_counter() == 'B':
            # Check if blue is moving a piece
            if from_value[0] != 'B':
                return False
        else:
            # Check if red is moving a piece
            if from_value[0] != 'R':
                return False

        # check if player is in check, if so, confirms that the player is moving their general. If not, returns False.
        if self.get_player_counter() == 'R':
            if self._red_check is True:
                if from_value != 'RGE':
                    return False
        else:
            if self._blue_check is True:
                if from_value != 'BGE':
                    return False

        # check if the player is passing a turn
        if from_pos == to_pos:
            if self._player_counter == 'B':
                self._player_counter = 'R'
                self._next_player = 'B'
            else:
                self._player_counter = 'B'
                self._next_player = 'R'
            return True

        results = 0

        # there are two piece codes with G. Algorithm checks which is being moved.
        if from_value[1] == 'G':

            # if piece is a guard, checks move and moves it if valid
            if from_value[2] == 'D':
                results = self.check_guard(from_pos, to_pos, to_value)

            # if piece is the general checks move and moves it if valid
            elif from_value[2] == 'E':
                results = self.check_general(from_pos, to_pos, to_value)

        # if piece is a soldier, checks move and moves it if valid
        elif from_value[1] == 'S':
            results = self.check_soldier(from_pos, to_pos, to_value)

        # if piece is a horse, checks move and moves it if valid
        elif from_value[1] == 'H':
            results = self.check_horse(from_pos, to_pos, to_value)

        # if piece is an elephant, checks move and moves it if valid
        elif from_value[1] == 'E':
            results = self.check_elephant(from_pos, to_pos, to_value)

        # there are two piece codes with C. Algorithm checks which is being moved
        elif from_value[1] == 'C':

            # if piece is a chariot, checks move and moves it if valid
            if from_value[2] == 'H':
                results = self.check_chariot(from_pos, to_pos)

            # if piece is a cannon, checks move and moves it if valid
            if from_value[2] == 'A':
                results = self.check_cannon(from_pos, to_pos)

        if results is True:

            self._board[from_pos] = ' '
            self._board[to_pos] = from_value

            # check if any general is in check as a result of the move
            gen_check = self.check_checker()
            if gen_check[0] == 1:

                # if move places own general in check, undo the move and return False
                if gen_check[1] == self.get_player_counter():
                    self._board[from_pos] = from_value
                    self._board[to_pos] = to_value
                    return False

                # if opposing general, places other team in check and checks for a checkmate
                else:
                    if gen_check[1] == 'R':
                        self._red_check = True
                        in_checkmate = self.is_checkmate()
                        if in_checkmate is True:
                            self._game_state = 'BLUE_WON'
                    else:
                        self._blue_check = True
                        in_checkmate = self.is_checkmate()
                        if in_checkmate is True:
                            self._game_state = 'RED_WON'

            # change whose turn it is
            if self._player_counter == 'B':
                self._player_counter = 'R'
                self._next_player = 'B'
            else:
                self._player_counter = 'B'
                self._next_player = 'R'
            return True
        else:
            return False

    def check_soldier(self, from_pos, to_pos, to_value, check=0):
        """Checks if the soldier's move is valid and then checks if a piece is captured. Soldiers can move one step
        forward (towards enemy palace) or sideways. They can also move diagonally if they are in the palace. Uses the
        get_piece_move method to calculate valid moves."""

        possible_moves1 = self.get_piece_move(1, 0, from_pos)
        possible_moves2 = self.get_piece_move(0, 1, from_pos)
        possible_moves = possible_moves1 + possible_moves2

        if from_pos in self.get_palace():
            extra_moves = self.get_piece_move(1, 1, from_pos)
            for extramove in extra_moves:
                if extramove in self.get_palace():
                    possible_moves.append(extramove)

        from_value = self.get_board()[from_pos]

        from_len = len(from_pos)
        if from_len == 2:
            from_row = int(from_pos[1])
        if from_len == 3:
            from_row = int(from_pos[1] + from_pos[2])

        # looks for the backwards moves and removes them for a blue soldier (includes palace moves)
        if from_value[0] == 'B':
            moves_to_remove = []

            for potential_move in possible_moves:
                potential_len = len(potential_move)
                if potential_len == 2:
                    potential_row = int(potential_move[1])
                if potential_len == 3:
                    potential_row = int(potential_move[1] + potential_move[2])

                if self._row_range[potential_row] > self._row_range[from_row]:
                    moves_to_remove.append(potential_move)

            for move in moves_to_remove:
                possible_moves.remove(move)

        # looks for the backwards moves and removes them for a red soldier (includes palace moves)
        if from_value[0] == 'R':
            moves_to_remove = []

            for potential_move in possible_moves:
                potential_len = len(potential_move)
                if potential_len == 2:
                    potential_row = int(potential_move[1])
                if potential_len == 3:
                    potential_row = int(potential_move[1] + potential_move[2])

                if self._row_range[potential_row] < self._row_range[from_row]:
                    moves_to_remove.append(potential_move)

            for move in moves_to_remove:
                possible_moves.remove(move)

        if check == 1:
            return possible_moves

        if to_pos not in possible_moves:
            return False
        elif to_value[0] == self.get_player_counter():
            return False
        else:
            return True

    def check_cannon(self, from_pos, to_pos, check=0):
        """Checks if the cannon's move is valid and then checks if a piece is captured. Can move orthogonally as long as
        there is a piece for the cannon to jump over in between where the cannon wants to go and where the cannon is.
        The piece can be friendly or not. The cannon may also move diagonally in the palace as long as it can hop over
        a piece. Cannons cannot jump other cannons and may not capture other cannons. This method does not use the
        get_piece_move method to calculate valid moves. Instead, has its own algorithm to calculate valid moves."""

        from_len = len(from_pos)
        if from_len == 2:
            from_column = from_pos[0]
            from_row = int(from_pos[1])
        if from_len == 3:
            from_column = from_pos[0]
            from_row = int(from_pos[1] + from_pos[2])

        if check == 0:
            to_len = len(to_pos)
            if to_len == 2:
                to_column = to_pos[0]
                to_row = int(to_pos[1])
            if to_len == 3:
                to_column = to_pos[0]
                to_row = int(to_pos[1] + to_pos[2])

        # position in range for origins row and column
        index_column = self._column_range.index(from_column)
        index_row = self._row_range.index(from_row)

        if check == 0:
            # check if move is valid for regular moves not in palace
            if from_column != to_column and from_row != to_row and (from_pos not in self._palace):
                return False

        # stops for each direction in loop and the loop stop
        up = down = left = right = stop = False
        # check for first jumped piece
        jup = jdown = jleft = jright = False
        counter = 0
        possible_moves = []

        # loop finds the valid moves that the cannon can move in each direction (not in palace)
        while not stop:
            counter += 1

            if up is False:
                # check if next move up is on board
                if (index_row - counter) < 0:
                    up = True

                # if a valid unit has been jumped, begins to write valid moves
                elif jup is True:
                    trow = self._row_range[index_row - counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, a cannon, or empty and acts accordingly
                    if check_value[0] == ' ':
                        possible_moves.append(check_key)
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        up = True
                    elif check_value[0] == self.get_player_counter():
                        up = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        up = True

                # looks for a valid unit to count as jumped
                else:
                    trow = self._row_range[index_row - counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if space has a friend or foe piece or a cannon from either team
                    if check_value[0] == ' ':
                        pass
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        up = True
                    elif check_value[0] == self.get_player_counter():
                        jup = True
                    elif check_value[0] == self.get_next_player():
                        jup = True

            if down is False:
                # check if next move down is on board
                if (index_row + counter) > 9:
                    down = True

                elif jdown is True:
                    trow = self._row_range[index_row + counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, a cannon, or empty and acts accordingly
                    if check_value[0] == ' ':
                        possible_moves.append(check_key)
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        down = True
                    elif check_value[0] == self.get_player_counter():
                        down = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        down = True
                else:
                    trow = self._row_range[index_row + counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if space has a friend or foe piece or a cannon from either team
                    if check_value[0] == ' ':
                        pass
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        down = True
                    elif check_value[0] == self.get_player_counter():
                        jdown = True
                    elif check_value[0] == self.get_next_player():
                        jdown = True

            if left is False:
                # check if next move left is on board
                if (index_column - counter) < 0:
                    left = True

                elif jleft is True:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column - counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, a cannon, or empty and acts accordingly
                    if check_value[0] == ' ':
                        possible_moves.append(check_key)
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        left = True
                    elif check_value[0] == self.get_player_counter():
                        left = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        left = True

                else:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column - counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == ' ':
                        pass
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        left = True
                    elif check_value[0] == self.get_player_counter():
                        jleft = True
                    elif check_value[0] == self.get_next_player():
                        jleft = True

            if right is False:
                # check if next move right is on board
                if (index_column + counter) > 8:
                    right = True

                elif jright is True:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column + counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == ' ':
                        possible_moves.append(check_key)
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        right = True
                    elif check_value[0] == self.get_player_counter():
                        right = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        right = True
                else:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column + counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == ' ':
                        pass
                    elif check_value[1] == 'C' and check_value[2] == 'A':
                        right = True
                    elif check_value[0] == self.get_player_counter():
                        jright = True
                    elif check_value[0] == self.get_next_player():
                        jright = True
            if (up is True) and (down is True) and (left is True) and (right is True):
                stop = True

        # if cannon is in palace, finds extra available moves if there are any
        if from_pos in self.get_palace():
            if from_column == 'd' or from_column == 'f':
                if from_row != 2 or from_row != 9:
                    jmp_check = self.get_piece_move(1, 1, from_pos)
                    extra_moves = self.get_piece_move(2, 2, from_pos)
                    for pmove in extra_moves:
                        if pmove in self.get_palace() and self.get_board()[pmove][0] != self.get_player_counter():
                            for jmp in jmp_check:
                                if jmp in self.get_palace() and self.get_board()[jmp] != ' ':
                                    possible_moves.append(pmove)

        if check == 1:
            return possible_moves

        if to_pos not in possible_moves:
            return False
        else:
            return True

    def check_chariot(self, from_pos, to_pos, check=0):
        """Checks if the chariot's move is valid and then checks if a piece is captured. The chariot can move
        orthogonally as far as they want. They may also move diagonally in the palace. This method does not use the
        get_piece_move method to calculate valid moves. Instead uses own algorithm to calculate valid moves."""

        from_len = len(from_pos)
        if from_len == 2:
            from_column = from_pos[0]
            from_row = int(from_pos[1])
        if from_len == 3:
            from_column = from_pos[0]
            from_row = int(from_pos[1] + from_pos[2])

        if check == 0:
            to_len = len(to_pos)
            if to_len == 2:
                to_column = to_pos[0]
                to_row = int(to_pos[1])
            if to_len == 3:
                to_column = to_pos[0]
                to_row = int(to_pos[1] + to_pos[2])

        # position in range for origins row and column
        index_column = self._column_range.index(from_column)
        index_row = self._row_range.index(from_row)

        if check == 0:
            # check if move is valid for regular moves not in palace
            if from_column != to_column and from_row != to_row and (from_pos not in self._palace):
                return False

        # stops for each direction in loop and the loop stop
        up = down = left = right = stop = False
        counter = 0
        possible_moves = []

        # loop finds the valid moves that the chariot can move in each direction (not in palace)
        while not stop:
            counter += 1
            if up is False:
                # check if next move up is on board
                if (index_row - counter) < 0:
                    up = True
                else:
                    trow = self._row_range[index_row - counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == self.get_player_counter():
                        up = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        up = True
                    else:
                        possible_moves.append(check_key)
            if down is False:
                # check if next move down is on board
                if (index_row + counter) > 9:
                    down = True
                else:
                    trow = self._row_range[index_row + counter]
                    tcol = self._column_range[index_column]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == self.get_player_counter():
                        down = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        down = True
                    else:
                        possible_moves.append(check_key)
            if left is False:
                # check if next move left is on board
                if (index_column - counter) < 0:
                    left = True
                else:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column - counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == self.get_player_counter():
                        left = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        left = True
                    else:
                        possible_moves.append(check_key)
            if right is False:
                # check if next move right is on board
                if (index_column + counter) > 8:
                    right = True
                else:
                    trow = self._row_range[index_row]
                    tcol = self._column_range[index_column + counter]
                    check_key = tcol + str(trow)
                    check_value = self.get_board()[check_key]

                    # check if move contains a friend, foe, or empty and acts accordingly
                    if check_value[0] == self.get_player_counter():
                        right = True
                    elif check_value[0] == self.get_next_player():
                        possible_moves.append(check_key)
                        right = True
                    else:
                        possible_moves.append(check_key)
            if (up is True) and (down is True) and (left is True) and (right is True):
                stop = True

        # if chariot is in palace, finds extra available moves
        if from_pos in self.get_palace():
            if from_row == 2 or from_row == 9 or from_column == 'E':
                extra_moves = self.get_piece_move(1, 1, from_pos)
                for pmove in extra_moves:
                    if pmove in self.get_palace() and self.get_board()[pmove][0] != self.get_player_counter():
                        possible_moves.append(pmove)
            else:
                extra_moves = self.get_piece_move(1, 1, from_pos) + self.get_piece_move(2, 2, from_pos)
                for pmove in extra_moves:
                    if pmove in self.get_palace() and self.get_board()[pmove][0] != self.get_player_counter():
                        possible_moves.append(pmove)

        if check == 1:
            return possible_moves

        if to_pos not in possible_moves:
            return False
        else:
            return True

    def check_elephant(self, from_pos, to_pos, to_value, check=0):
        """Checks if the elephant's move is valid and then checks if a piece is captured. The elephant moves one step
        orthogonally and then two steps diagonally. This method uses the get_piece_move method to find valid moves
        for the elephant piece to be moved."""

        possible_moves1 = self.get_piece_move(3, 2, from_pos)
        possible_moves2 = self.get_piece_move(2, 3, from_pos)
        possible_moves = possible_moves1 + possible_moves2

        if check == 1:
            return possible_moves

        if to_pos not in possible_moves:
            return False
        elif to_value[0] == self.get_player_counter():
            return False
        else:
            return True

    def check_horse(self, from_pos, to_pos, to_value, check=0):
        """Checks if the horse's move is valid and then checks if a piece is captured. The horse can move orthogonally
        once then diagonally once. This method uses the get_piece_move method to find valid moves for the horse piece
        that is to be moved."""

        possible_moves1 = self.get_piece_move(2, 1, from_pos)
        possible_moves2 = self.get_piece_move(1, 2, from_pos)
        possible_moves = possible_moves1 + possible_moves2

        if check == 1:
            return possible_moves

        if to_pos not in possible_moves:
            return False
        elif to_value[0] == self.get_player_counter():
            return False
        else:
            return True

    def check_guard(self, from_pos, to_pos, to_value, check=0):
        """Checks if the guard's move is valid and then checks if a piece is captured. The guard can
        move one step any direction within the palace. This method uses the get_piece_move method to find valid moves
        for the guard."""

        possible_moves1 = self.get_piece_move(1, 0, from_pos)
        possible_moves2 = self.get_piece_move(0, 1, from_pos)
        possible_moves3 = self.get_piece_move(1, 1, from_pos)
        moves_to_check = possible_moves1 + possible_moves2 + possible_moves3

        possible_moves = []
        for move in moves_to_check:
            if move in self.get_palace():
                possible_moves.append(move)

        if check == 1:
            return possible_moves

        if to_pos not in self.get_palace():
            return False
        elif to_pos not in possible_moves:
            return False
        elif to_value[0] == self.get_player_counter():
            return False
        else:
            return True

    def check_general(self, from_pos, to_pos, to_value):
        """Checks if the general's move is valid and then checks if a piece is captured.  The general can move one step
        any direction within the palace. This method uses the get_piece_move method to find valid moves for the general.
        This method also checks to make sure that the move does not put the general in check."""

        possible_moves1 = self.get_piece_move(1, 0, from_pos)
        possible_moves2 = self.get_piece_move(0, 1, from_pos)
        possible_moves3 = self.get_piece_move(1, 1, from_pos)
        moves_to_check = possible_moves1 + possible_moves2 + possible_moves3

        possible_moves = []
        for move in moves_to_check:
            if move in self.get_palace():
                possible_moves.append(move)

        if to_pos not in self.get_palace():
            return False
        elif to_pos not in possible_moves:
            return False
        elif to_value[0] == self.get_player_counter():
            return False
        else:

            # make sure the general is not putting himself in check
            from_value = self._board[from_pos]
            curr_to_pos_value = self._board[to_pos]

            self._board[from_pos] = ' '
            self._board[to_pos] = from_value

            position_check = self.check_checker(1)
            if position_check[0] == 1:
                return False

            self._board[from_pos] = from_value
            self._board[to_pos] = curr_to_pos_value

            if self._blue_check is True:
                self._blue_check = False
            if self._red_check is True:
                self._red_check = False

            return True

    def get_piece_move(self, row_change, column_change, origin):
        """Returns moves that the piece can make given the amount the piece moves by row and then the amount the piece
        moves by column. Also needs the position of the piece currently. Does not check if the move is valid or not.
        For example, two functions calls would be needed for a horse since it can move 1 row and 2 columns or
        it can move 2 rows and 1 column. This would encapsulate all the valid moves a horse could make (as long as they
        are on the board and do not have a piece from its own team occupying the space)."""

        # range for each direction of a move
        row_range = self._row_range
        column_range = self._column_range

        # break up board space code
        origin_len = len(origin)
        if origin_len == 2:
            column = origin[0]
            row = int(origin[1])
        if origin_len == 3:
            column = origin[0]
            row = int(origin[1] + origin[2])

        # position in range for origins row and column
        index_column = column_range.index(column)
        index_row = row_range.index(row)

        # list of moves
        moves = []

        # checks for four possible moves with given coordinates and appends to moves if valid. Also checks for if the
        # move is blocked
        if (index_row - row_change) >= 0 and (index_column - column_change) >= 0:

            if column_change == 0 or row_change == 0 or column_change == row_change:
                move = column_range[index_column - column_change] + str(row_range[index_row - row_change])
                if move not in moves:
                    moves.append(move)
            elif column_change > row_change:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while row_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column - column_check] + str(row_range[index_row - row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column - column_change] + str(row_range[index_row - row_change])
                    moves.append(move)
            else:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while column_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column - column_check] + str(row_range[index_row - row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column - column_change] + str(row_range[index_row - row_change])
                    moves.append(move)

        if (index_row - row_change) >= 0 and (index_column + column_change) < 9:

            if column_change == 0 or row_change == 0 or column_change == row_change:
                move = column_range[index_column + column_change] + str(row_range[index_row - row_change])
                if move not in moves:
                    moves.append(move)
            elif column_change > row_change:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while row_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column + column_check] + str(row_range[index_row - row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column + column_change] + str(row_range[index_row - row_change])
                    moves.append(move)
            else:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while column_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column + column_check] + str(row_range[index_row - row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column + column_change] + str(row_range[index_row - row_change])
                    moves.append(move)

        if (index_row + row_change) < 10 and (index_column + column_change) < 9:

            if column_change == 0 or row_change == 0 or column_change == row_change:
                move = column_range[index_column + column_change] + str(row_range[index_row + row_change])
                if move not in moves:
                    moves.append(move)
            elif column_change > row_change:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while row_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column + column_check] + str(row_range[index_row + row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column + column_change] + str(row_range[index_row + row_change])
                    moves.append(move)
            else:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while column_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column + column_check] + str(row_range[index_row + row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column + column_change] + str(row_range[index_row + row_change])
                    moves.append(move)

        if (index_row + row_change) < 10 and (index_column - column_change) >= 0:

            if column_change == 0 or row_change == 0 or column_change == row_change:
                move = column_range[index_column - column_change] + str(row_range[index_row + row_change])
                if move not in moves:
                    moves.append(move)
            elif column_change > row_change:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while row_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column - column_check] + str(row_range[index_row + row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column - column_change] + str(row_range[index_row + row_change])
                    moves.append(move)
            else:
                row_check = row_change
                column_check = column_change
                blocked_check = False
                while column_check != 0:
                    row_check -= 1
                    column_check -= 1
                    block_key = column_range[index_column - column_check] + str(row_range[index_row + row_check])
                    block_value = self.get_board()[block_key]
                    if block_value != ' ':
                        blocked_check = True
                if blocked_check is not True:
                    move = column_range[index_column - column_change] + str(row_range[index_row + row_change])
                    moves.append(move)

        return moves

    def check_checker(self, checkmate_check=0):
        """Checks if a move will result in either general being in check. Does this by simulating all moves that every
        piece on the board can make. If any of the simulated possible moves include the opposing teams general, then
        the player with that general will be marked as in check in the Return."""

        all_keys = self.get_board().keys()

        for key in all_keys:
            value = self.get_board()[key]
            if value == ' ':
                continue

            if checkmate_check == 1 and value[0] == self.get_next_player():
                continue

            if value[1] == 'S':
                moves = self.check_soldier(key, 0, '0', 1)
            elif value[1] == 'H':
                moves = self.check_horse(key, 0, '0', 1)
            elif value[1] == 'E':
                moves = self.check_elephant(key, 0, '0', 1)
            elif value[1] == 'C':
                if value[2] == 'H':
                    moves = self.check_chariot(key, 0, 1)
                if value[2] == 'A':
                    moves = self.check_cannon(key, 0, 1)
            else:
                continue

            for key2 in moves:
                if self.get_board()[key2] == ' ':
                    continue
                elif self.get_board()[key2][1] == 'G' and self.get_board()[key2][2] == 'E':
                    if self.get_board()[key2][0] == self.get_board()[key][0]:
                        continue
                    else:
                        if self.get_board()[key][0] == 'R':
                            blue_check = [1, 'B']
                            return blue_check
                        else:
                            red_check = [1, 'R']
                            return red_check

        return [0]

    def is_checkmate(self):
        """Checks if a general has an available move when a check is called. Will do this by making a check where all
        the enemy team remaining pieces can move and mark the spaces surrounding the general. If there is an available
        space (a space that is not marked) then the game state is not changed. If there is not an available space, then
        the method will check all the team in checks available units to see if a piece can intervene for the general. If
        the player fails both of these checks, then that player is marked as in checkmate and the game is over."""

        all_keys = self.get_board().keys()

        # first checks if moving the general will get the player out of check
        for key in all_keys:
            value = self.get_board()[key]
            if value == 'RGE' or value == 'BGE':

                # break up key into row and column parts and then finding index in row and column list
                key_len = len(key)
                if key_len == 2:
                    column = key[0]
                    row = int(key[1])
                if key_len == 3:
                    column = key[0]
                    row = int(key[1] + key[2])

                index_column = self._column_range.index(column)
                index_row = self._row_range.index(row)

                # make list of all the keys around the general being checked that are on the board
                potential_moves = []
                if (index_row - 1) >= 0 and (index_column - 1) >= 0:
                    move = self._column_range[index_column - 1] + str(self._row_range[index_row - 1])
                    potential_moves.append(move)
                if (index_row - 1) >= 0 and (index_column + 1) < 9:
                    move = self._column_range[index_column - 1] + str(self._row_range[index_row + 1])
                    potential_moves.append(move)
                if (index_row + 1) < 10 and (index_column + 1) < 9:
                    move = self._column_range[index_column + 1] + str(self._row_range[index_row + 1])
                    potential_moves.append(move)
                if (index_row + 1) < 10 and (index_column - 1) >= 0:
                    move = self._column_range[index_column + 1] + str(self._row_range[index_row - 1])
                    potential_moves.append(move)
                if (index_row - 1) >= 0:
                    move = self._column_range[index_column] + str(self._row_range[index_row - 1])
                    potential_moves.append(move)
                if (index_row + 1) < 10:
                    move = self._column_range[index_column] + str(self._row_range[index_row + 1])
                    potential_moves.append(move)
                if (index_column - 1) >= 0:
                    move = self._column_range[index_column - 1] + str(self._row_range[index_row])
                    potential_moves.append(move)
                if (index_column + 1) < 9:
                    move = self._column_range[index_column + 1] + str(self._row_range[index_row])
                    potential_moves.append(move)

                # narrow keys to moves available around general that are in the palace and available to move to
                remove = []
                for check in potential_moves:
                    if check not in self.get_palace():
                        remove.append(check)
                    elif self.get_board()[check][0] == value[0]:
                        remove.append(check)
                for item in remove:
                    potential_moves.remove(item)

                # add place general is in as a potential move to make checking for moves easier
                potential_moves.append(key)

                # check if keys would place the general in check by simulating a move by the general to that place
                # will delete that move if it does not pass the check.
                remove2 = []
                for check2 in potential_moves:
                    from_pos = key
                    to_pos = check2
                    curr_to_pos_value = self._board[to_pos]

                    self._board[from_pos] = ' '
                    self._board[to_pos] = value

                    position_check = self.check_checker(1)
                    if position_check[0] == 1:
                        remove2.append(check2)

                    self._board[from_pos] = value
                    self._board[to_pos] = curr_to_pos_value
                for item in remove2:
                    potential_moves.remove(item)

                # check if there are any available moves left. If there is one, returns False
                if len(potential_moves) != 0:
                    return False

        # next checks if any of the pieces can intervene for the general to get it out of check
        for key in all_keys:
            value = self.get_board()[key]

            if value == ' ':
                continue

            # figure out which piece we are looking at and get valid moves for the piece at current position
            if value[1] == 'S':
                moves = self.check_soldier(key, 0, '0', 1)
            elif value[1] == 'H':
                moves = self.check_horse(key, 0, '0', 1)
            elif value[1] == 'E':
                moves = self.check_elephant(key, 0, '0', 1)
            elif value[1] == 'C':
                if value[2] == 'H':
                    moves = self.check_chariot(key, 0, 1)
                if value[2] == 'A':
                    moves = self.check_cannon(key, 0, 1)
            elif value[1] == 'G':
                if value[2] == 'D':
                    moves = self.check_guard(key, 0, '0', 1)
            else:
                continue

            # see if any of the valid moves will remove the check status. If so, will return False.
            for key2 in moves:
                from_pos = key
                to_pos = key2
                curr_to_pos_value = self._board[key]

                self._board[from_pos] = ' '
                self._board[to_pos] = value

                position_check = self.check_checker(1)
                if position_check[0] == 0:
                    return False

                self._board[from_pos] = value
                self._board[to_pos] = curr_to_pos_value

        # if neither check passes, then it is checkmate.
        return True
