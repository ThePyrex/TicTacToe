# Tic-Tac-Toe with ChatGPT

Welcome to this Python-based Tic-Tac-Toe game that also incorporates the power of ChatGPT for AI-powered moves. This game allows you to play Tic-Tac-Toe against an AI opponent, represented by ChatGPT, using the OpenAI API.

## Prerequisites
To run this code, you'll need to install the OpenAI Python package and have an API key. You can sign up for the OpenAI API and obtain an API key from the OpenAI platform. Once you have your API key, replace the placeholder `openai.api_key` with your actual API key.

## How to Play
1. The game board is represented as a list of 9 slots, where each slot is initially marked with a '-'. The indices on the board are as follows:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

2. The game starts with "X" as the first player and "O" as the ChatGPT AI opponent. Players take turns to make a move.

3. When it's your turn, you will be prompted to enter a number between 1 and 9. This number corresponds to the index on the board where you want to place your mark.

4. The game will check for horizontal, vertical, and diagonal wins, as well as ties, after each move.

5. If a win is detected, the game will declare the winner and end.

6. If all slots are filled without a winner, the game will declare a tie and end.

7. The game will switch between you and ChatGPT until there's a winner or a tie.

8. ChatGPT will make its moves based on the input you provide, so make sure to follow the prompt and choose a free spot on the board.
