import openai

openai.api_key = "your API key"

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True

# Printing board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player Input
def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    elif board[inp-1] == "X" or "O":
        print("Place is already taken. Retry")
        playerInput(board)
    else:
        print("Give a valid number as Input!")

#check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
    
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
    
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False
        return True

def checkwin():
    global winner
    global gameRunning
    if checkRow(board) or checkDiagonal(board) or checkHorizontal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False
        return True

def integerFilter(move):
    if not isinstance(move, int):
        for letter in move:
            if letter.isdigit():
                move = int(letter)
                return move
    else: 
        move = int(move)
        return move

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else: currentPlayer = "X"

# ChatGPT
def chatgpt(board):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "Your response should be a single number from 1 to 9. The number represents the index in this list board."},
        {"role": "user", "content": f"Please choose a free '-' spot on the 3x3 Tic-Tac-Toe board: {board}"},
    ]
    )
    move = response['choices'][0]['message']['content']
    move = integerFilter(move)
    if board[move - 1] == "-":
        board[move - 1] = "O"
    else:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
        {"role": "system", "content": "Your response should be a single number from 1 to 9. The number represents the index in this list board."},
        {"role": "user", "content": f"This place is already taken. Try again: 3x3 Tic-Tac-Toe board: {board}"},
        ]
        )
        move = response['choices'][0]['message']['content']
        move = integerFilter(move)
        if board[move - 1] == "-":
            board[move - 1] = "O"

while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkwin():
        break
    if checkTie(board):
        break
    switchPlayer()
    chatgpt(board)
    if checkwin():
        break
    if checkTie(board):
        break
    switchPlayer()
