import itertools

def get_file_moves(position: str) -> list[str]:  # position = A1
    file, *_ = [char for char in position]
    file = file.upper()
    file_ordinal = ord(file)
    low_file_limit = ord('A')
    high_file_limit = ord('H')
    file_moves: list[str] = []

    for offset in range(1,3):
        right_move = file_ordinal + offset
        left_move = file_ordinal - offset

        if low_file_limit <= right_move <= high_file_limit:
            file_moves.append(chr(right_move))

        if low_file_limit <= left_move <= high_file_limit:
            file_moves.append(chr(left_move))

    return file_moves

def get_rank_moves(position: str) -> list[str]:  # position = A1
    _, rank = position
    rank = int(rank)
    low_rank_limit = 1
    high_rank_limit = 8
    rank_moves: list[str] = []

    for offset in range(1,3):
        up_move = rank + offset
        down_move = rank - offset

        if low_rank_limit <= up_move <= high_rank_limit:
            rank_moves.append(up_move)

        if low_rank_limit <= down_move <= high_rank_limit:
            rank_moves.append(down_move)

    return rank_moves


def knight_moves(position):
    file, rank = [*position]
    file = file.upper()
    rank = int(rank)
    file_ordinal = ord(file)
    file_moves = sorted(get_file_moves(position))
    rank_moves = sorted(get_rank_moves(position))

    # combine permutations and count number of blocks moved. If we've moved 3 blocks, add to list of valid moves

    moves_of_one = [move for move in file_moves if abs(file_ordinal - ord(move)) == 1]
    moves_of_one.extend([move for move in rank_moves if abs(rank - move) == 1])
    moves_of_two = [move for move in file_moves if abs(file_ordinal - ord(move)) == 2]
    moves_of_two.extend([move for move in rank_moves if abs(rank - move) == 2])

    files_of_one = [item for item in moves_of_one if isinstance(item, str)]
    ranks_of_one = [item for item in moves_of_one if isinstance(item, int)]
    files_of_two = [item for item in moves_of_two if isinstance(item, str)]
    ranks_of_two = [item for item in moves_of_two if isinstance(item, int)]

    # moves = [itertools.product(files_of_one, ranks_of_two), itertools.product(files_of_two, ranks_of_one)]
    moves = list(itertools.chain(
        itertools.product(files_of_one, ranks_of_two),
        itertools.product(files_of_two, ranks_of_one)
    ))

    return len(moves)

move_count = knight_moves('d4')
print(move_count) 