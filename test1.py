import chess
import chess.pgn
import efish

pgn = open("board/sample_game.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()

counter = 0

for move in game.mainline_moves(): #iterate through the sample game to the position currently being tested

    board.push(move)

    if counter == 66:
        break

    counter += 1
    
position = board

print(position)

move_list = efish.evaluate(position, 4) #returns list of moves sorted by evaluation with search depth 4

print(move_list)

new_position = efish.play_best_move(position, move_list)

print(new_position)