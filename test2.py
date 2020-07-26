import chess
import chess.pgn
import efish

pgn = open("board/fen1.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()
    
position = board

print(position)

move_list = efish.evaluate(position, 6) #returns list of moves sorted by evaluation with search depth 4

print(move_list)

new_position = efish.play_best_move(position, move_list)

print(new_position)