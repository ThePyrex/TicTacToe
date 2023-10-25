import openai

openai.api_key = "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"

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True
correct = True
costs = 0
count = 0

# Printing board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player Input
def playerInput(board):
    try:
        inp = int(input("Enter a number between 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer

        elif board[inp-1] == "X" or board[inp-1] == "O":
            print("Place is already taken. Retry")
            playerInput(board)

        else:
            print("Give a valid number as Input!")
            
    except ValueError:
        print("Please enter a valid integer between 1 and 9.")
        playerInput(board)

    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False
        return True

def checkWin(board):
    global winner
    if  (board[0] == board[1] == board[2] and board[0] != "-") or \
        (board[3] == board[4] == board[5] and board[3] != "-") or \
        (board[6] == board[7] == board[8] and board[6] != "-") or \
        (board[0] == board[3] == board[6] and board[0] != "-") or \
        (board[1] == board[4] == board[7] and board[1] != "-") or \
        (board[2] == board[5] == board[8] and board[2] != "-") or \
        (board[0] == board[4] == board[8] and board[0] != "-") or \
        (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
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

def counting_costs(response):
    global count
    global costs
    costs += response['usage']['total_tokens']
    count += 1

def check_game_end(board):
    if checkWin(board) or checkTie(board):
        return True
    return False

# ChatGPT
def chatgpt(board):
    response = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages = [
        {"role": "system", "content": f"You are player 'O' and you want to win this tic tac toe game. Use this board information {board} and answer with a number from 1-9 where you want to put you 'O'."},
        {"role": "user", "content": f"Please choose a free '-' spot on the 3x3 Tic-Tac-Toe board: {board}"},
    ]
    )
    move = response['choices'][0]['message']['content']
    move = integerFilter(move)
    if board[move - 1] == "-":
        board[move - 1] = "O"
        counting_costs(response)
    else:
        print("Second try needed")
        response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages = [
        {"role": "system", "content": f"You are player 'O' and you want to win this tic tac toe game. Use this board information {board} and answer with a number from 1-9 where you want to put you 'O'."},
        {"role": "user", "content": f"This place is already taken. Try again: 3x3 Tic-Tac-Toe board: {board}"},
        ]
        )
        move = response['choices'][0]['message']['content']
        move = integerFilter(move)
        if board[move - 1] == "-":
            board[move - 1] = "O"
            counting_costs(response)

def main_game_loop():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        
        if check_game_end(board):
            printBoard(board)
            print(f"The Winner is player {winner}")
            print(f"The Total costs for this game which consisted of {count} requests where: {costs} tokens")
            break
        
        switchPlayer()
        chatgpt(board)
        switchPlayer()

main_game_loop()
