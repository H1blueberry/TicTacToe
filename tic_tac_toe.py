import sys
import copy
sys.setrecursionlimit(1000)


def check_field(fields, player1, player2, field):
    if field not in player1 and field not in player2 and field in fields:
        return True
    return False


def generate_field(fields2, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return None
    board = copy.deepcopy(fields2)
    player_copy = copy.deepcopy(player)
    player2_copy = copy.deepcopy(player2)
    field, x = best_player2(board, player_copy, player2_copy)
    return field


def best_player(board, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return "a", utility(player, player2)
    v = 2
    for move in board:
        board2 = copy.deepcopy(board)
        board2.remove(move)
        player_2 = copy.deepcopy(player)
        player_2.append(move)
        x, v_other = best_player2(board2, player_2, player2)
        if v > v_other:
            v = v_other
            best = move
    return best, v


def best_player2(board, player, player2):
    if check_win(player) or check_win(player2) or (len(player)) + (len(player2)) == 9:
        return "a", utility(player, player2)
    v = -2
    for move in board:
        board2 = copy.deepcopy(board)
        board2.remove(move)
        player2_2 = copy.deepcopy(player2)
        player2_2.append(move)
        x, v_other = best_player(board2, player, player2_2)
        if v < v_other:
            v = v_other
            best = move
    return best, v


def utility(player, player2):
    if check_win(player):
        return -1
    elif check_win(player2):
        return 1
    else:
        return 0


def check_win(player):
    if "upper_left" in player and "upper_middle" in player and "upper_right" in player or "middle_left" in player and "middle_middle" in player and "middle_right" in player or "bottom_left" in player and "bottom_middle" in player and "bottom_right" in player or "upper_left" in player and "middle_middle" in player and "bottom_right" in player or "upper_right" in player and "middle_middle" in player and "bottom_left" in player or "upper_left" in player and "middle_left" in player and "bottom_left" in player or "upper_middle" in player and "middle_middle" in player and "bottom_middle" in player or "upper_right" in player and "middle_right" in player and "bottom_right" in player:
        return True
    return False
