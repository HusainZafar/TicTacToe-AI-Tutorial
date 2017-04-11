"""
Tic Tac Toe Minimax
"""

def display_board(board):
    """
    prints the current board
    """
    print "TIC TAC TOE                Move Index\n"
    print board[0] + " | " + board[1] + " | " + board[2] + "                     " + "0 1 2"
    print "--|---|---"
    print board[3] + " | " + board[4] + " | " + board[5] + "                     " + "3 4 5"
    print "--|---|---"
    print board[6] + " | " + board[7] + " | " + board[8] + "                     " + "6 7 8"
    print ""

def check_win(board, player1, player2):
    """
    returns status of current board: 1-> won, 2-> draw, 0-> game undecided
    if game won, return value is [1,who_won]
    """
    returned_val = ['', '']
    if board[0] == board[1] == board[2] and board[0] in [player1, player2]:
        returned_val = [1, board[0]]
    elif board[3] == board[4] == board[5] and board[3] in [player1, player2]:
        returned_val = [1, board[3]]
    elif board[6] == board[7] == board[8] and board[6] in [player1, player2]:
        returned_val = [1, board[6]]
    elif board[0] == board[3] == board[6] and board[0] in [player1, player2]:
        returned_val = [1, board[0]]
    elif board[1] == board[4] == board[7] and board[1] in [player1, player2]:
        returned_val = [1, board[1]]
    elif board[2] == board[5] == board[8] and board[2] in [player1, player2]:
        returned_val = [1, board[2]]
    elif board[0] == board[4] == board[8] and board[0] in [player1, player2]:
        returned_val = [1, board[0]]
    elif board[2] == board[4] == board[6] and board[2] in [player1, player2]:
        returned_val = [1, board[2]]
    elif '-' in board:
        returned_val = [0, board[0]]
    else:
        returned_val = [2, board[0]]
    return returned_val

def move_random(moves_list):
    """
    returns random index of one of the many possible moves
    """
    import random
    random = random.randrange(0, len(moves_list))
    return moves_list[random]

def the_move(board, lst):
    """
    returns a random index out of the best moves
    """
    max_val = max(lst)
    max_array = []
    for i in range(len(lst)):
        if lst[i] == max_val:
            max_array.append(i)
    k = move_random(max_array)
    cntr = 0
    for i in range(9):
        if board[i] == '-':
            cntr += 1
        if cntr == k+1:
            return i

def minimax(board, move, comp, plr):
    """
    Implements the minimax algorithm. Returns 1 : computer has won.
    Returns -1 when player wins.
    When it's the computer's turn and it has to return a value to its parent,
    the maximum value from the array is chosen else, the minimum value.
    """
    global COUNT
    COUNT += 1
    [is_win, who_won] = check_win(board, comp, plr)
    if is_win == 2:               
        return 0
    if is_win == 1:
        if who_won == comp:
            return 1
        if who_won == plr:
            return -1
    ret_list = []
    for i in range(9):
        if board[i] == '-':
            if move == comp:
                next_move = plr
            else:
                next_move = comp
            board[i] = move
            minimax_val = minimax(board, next_move, comp, plr)
            board[i] = '-'
            ret_list.append(minimax_val)
            COUNT -= 1
    if COUNT <= 1:
        return ret_list
    if move == comp:
        return max(ret_list)
    else:
        return min(ret_list)

def one_player(board):
    """
    function to play with the computer
    """
    order = int(raw_input("first(1) or second(2) ?\n"))
    comp = raw_input("Enter character for computer on board : ")
    plr = raw_input("Enter character for player on board   : ")
    global COUNT
    if order == 1:
        print "\033c"
        display_board(board)
        while check_win(board, comp, plr)[0] == 0:
            index = int(raw_input())
	    if index > 8:
	            print "\033c"
	            display_board(board)
		    continue
            # cant use already used index
            if board[index] != '-':
                print "\033c"
                display_board(board)
                continue
            board[index] = plr
            print "\033c"
            display_board(board)
            COUNT = 0
            if check_win(board, comp, plr)[0] != 0:
                break
            ret = minimax(board, comp, comp, plr)
            # chose move for computer
            board[the_move(board, ret)] = comp
            print "\033c"
            display_board(board)
        if check_win(board, comp, plr)[0] == 1:
            print "You lost!!"
        else:
            print "It's a draw!"

    if order == 2:
        while check_win(board, comp, plr)[0] == 0:
            COUNT = 0
            ret = minimax(board, comp, comp, plr)
            # chose move for computer
            board[the_move(board, ret)] = comp
            print "\033c"
            display_board(board)
            if check_win(board, comp, plr)[0] != 0:
                break
            # index already used can't be reused
            flag = 0
            while flag == 0:
                index = int(raw_input())
	    	if index > 8:
	            print "\033c"
	            display_board(board)
		    continue
                if board[index] == '-':
                    flag = 1
                    board[index] = plr
                    print "\033c"
                    display_board(board)
                else:
                    print "\033c"
                    display_board(board)

        if check_win(board, comp, plr)[0] == 1:
            print "You lost!!"
        else:
            print "It's a draw!"

if __name__ == "__main__":
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
    COUNT = 0
    one_player(board)
    #549946 iterarions minimax
    #upper limit 1+9*(1+8*(...(1+2*(1+1)...))
