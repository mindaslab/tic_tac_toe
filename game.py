from lib import *

message = """
Welcome to tic-tac-toe.
Your Symbol is 'O', the computer is 'X'.
"""
print(message)

board = Board()
agent = Agent()

while (not Winner.who(board)):
    print(board)
    human_move = input("Enter your position number:")
    human_move = int(human_move)
    board.play(human_move, 'O')
    print(board)
    agent_move = agent.move(board)
    board.play(agent_move, 'X')
    print("Computer has marked on " + str(agent_move))
    print(board)

print("Winner is " + Winner.who(board))
