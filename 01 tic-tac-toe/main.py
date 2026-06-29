def line_sum(a, b, c):
    return a + b + c

def print_board(xState, zState):
    print(f"{'X' if xState[0] else ('O' if zState[0] else ' ')} | {'X' if xState[1] else ('O' if zState[1] else ' ')} | {'X' if xState[2] else ('O' if zState[2] else ' ')}")
    print(f"--|---|---")
    print(f"{'X' if xState[3] else ('O' if zState[3] else ' ')} | {'X' if xState[4] else ('O' if zState[4] else ' ')} | {'X' if xState[5] else ('O' if zState[5] else ' ')}")
    print(f"--|---|---")
    print(f"{'X' if xState[6] else ('O' if zState[6] else ' ')} | {'X' if xState[7] else ('O' if zState[7] else ' ')} | {'X' if xState[8] else ('O' if zState[8] else ' ')}")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (line_sum(xState[win[0]], xState[win[1]], xState[win[2]])==3):
            print("X won the match!")
            return 1
        
        if (line_sum(zState[win[0]], zState[win[1]], zState[win[2]])==3):
            print("O won the match!")
            return 0
    return -1

def check_draw(xState, zState):
    return sum(xState) + sum(zState) == 9
        
if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]  
    zState = [0,0,0,0,0,0,0,0,0]
    
    turn = 1  # 1 for X's turn, 0 for O's turn
    
    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(xState, zState)
        if turn == 1:
            print("X's turn.")
            value = int(input("Enter a value: "))

            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("Cell already occupied. Try again.")
                continue

        else:
            print("O's turn.")
            value = int(input("Enter a value: "))

            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
            else:
                print("Cell already occupied. Try again.")
                continue
        cwin = checkWin(xState, zState)
        if (cwin != -1):
            break
        
        draw = check_draw(xState, zState)
        if draw:
            print("It's a Draw")
            break
        turn = 1 - turn  # Switch turns