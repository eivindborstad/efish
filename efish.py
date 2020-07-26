import chess
import chess.pgn

def evaluate(position, max_depth):

    #alpha beta pruning, calling heuristic function when depth is reached

    moves = position.legal_moves
    
    move_list = []
    
    current_depth = 1
        
    #alpha beta pruning
    
    alpha = -100000000
    beta = 100000000
    
    for move in moves:
       
        current_pos = position.copy()
        current_pos.push(move)
        
        eval = alpha_beta_pruning(current_pos, current_depth, max_depth, alpha, beta)
   
        move_list.append([move, eval])    
        
    #sort the moves
        
    def second(x):
    
        return x[1]
     
    if position.turn == chess.WHITE:
     
        move_list.sort(reverse=True, key=second)
        
    else:
        
        move_list.sort(reverse=False, key=second)
        
    for move in move_list:
    
        move[1] = real_eval(move[1])
    
    return move_list
    
    
def real_eval(eval): #can represent mate in X as well as numeric evaluations
    
        if eval > 999000: #if white can force checkmate
        
            return "M" + str(1000000 - eval)
            
        elif eval < -999000: #if black can force checkmate
        
            return "-M" + str(1000000 + eval)
            
        return eval #if nobody can force checkmate
 
def alpha_beta_pruning(position, current_depth, max_depth, alpha, beta):

    moves = position.legal_moves
    current_depth += 1
    
    if position.turn == chess.WHITE:
        
        eval = -100000000
        
    else:
    
        eval = 100000000
   
    for move in moves:
       
        current_pos = position.copy()
        current_pos.push(move)
        
        if position.turn == chess.WHITE:
        
            if current_depth == max_depth:
            
                eval = max(eval, heuristic_v1(current_pos, current_depth))
                
            else:
 
                eval = max(eval, alpha_beta_pruning(current_pos, current_depth, max_depth, alpha, beta))
                
            if eval >= beta:
            
                return eval
                
            if eval > alpha:
            
                alpha = eval
                
        if position.turn == chess.BLACK:
        
            if current_depth == max_depth:
            
                eval = min(eval, heuristic_v1(current_pos, current_depth))
                
            else:

                eval = min(eval, alpha_beta_pruning(current_pos, current_depth, max_depth, alpha, beta))  
                
            if eval <= alpha:
            
                return eval
                
            if eval < beta:
            
                beta = eval

    if eval == -100000000 or eval == 100000000: #if there are no legal moves, because game is already over
    
        return heuristic_v1(position, current_depth)
   
    return eval
    
   
def heuristic_v1(position, current_depth): #first version is simply material count or checking if won, lost or drawn

    evaluation = 0
    
    to_move = position.turn
    
    if position.is_checkmate():
    
        if to_move == chess.WHITE: #if white to move that means black is the one who has checkmated white
        
            return -1000000 + current_depth // 2
            
        else:
        
            return 1000000 - current_depth // 2
            
    if position.is_stalemate():
    
        return 0
        
    #material_count
        
    material_difference = 0
    material_difference_weight = 1
    
    piece_value_dict = {
        "P": 1,
        "N": 3,
        "B": 3, 
        "R": 5,
        "Q": 9,
        "p": -1, 
        "n": -3,
        "b": -3,
        "r": -5, 
        "q": -9,
        "K": 0,
        "k": 0, 
        "None": 0
    }
    
    for x in range(64):
    
        piece = str(position.piece_at(x))

        material_difference += piece_value_dict[piece]
        
    evaluation += material_difference * material_difference_weight
    
    return evaluation
    
    
    
    
    
def play_best_move(position, move_list):

    new_position = position.copy()
    new_position.push(move_list[0][0])
    return new_position
    