import chess
import chess.pgn


def evaluate(position, depth):

    #alpha beta pruning, calling heuristic function when depth is reached

    moves = position.legal_moves

    print(moves)
    
    move_list = []
    
    for move in moves:
       
        current_pos = position.copy()
        current_pos.push(move)
    
        eval = heuristic_v1(current_pos)
   
        move_list.append([move, eval])
        
    def second(x):
        
        return x[1]
     
    if position.turn == chess.WHITE:
     
        move_list.sort(reverse=True, key=second)
        
    else:
        
        move_list.sort(reverse=False, key=second)
    
    return move_list
    
    
    
   
def heuristic_v1(position): #first version is simply material count or checking if won, lost or drawn

    evaluation = 0
    
    to_move = position.turn
    
    if position.is_checkmate():
    
        if to_move == chess.WHITE: #if white to move that means black is the one who has checkmated white
        
            evaluation = -100
            
        else:
        
            evaluation = 100
    
    return evaluation
    
    
    
    
    
def play_best_move(position, move_list):

    new_position = position.copy()
    new_position.push(move_list[0][0])
    return new_position
    