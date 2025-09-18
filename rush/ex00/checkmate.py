def checkmate(board):
    board = board.strip().splitlines()
    size = len(board)

    kingr, kingc = -1, -1
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                kingr = r
                kingc = c
                break
        if kingr != -1:
            break

    if kingr == -1:
        print("Fail")
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r, c = kingr + dr, kingc + dc

        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]

            if piece != '.':
                is_straight = (dr == 0 or dc == 0)
                is_diagonal = (dr != 0 and dc != 0)

                if (is_straight and (piece == 'R' or piece == 'Q')) or \
                   (is_diagonal and (piece == 'B' or piece == 'Q')):
                    print("Success")
                    return

                break

            r = r + dr
            c = c + dc

    pawn_check_positions = [(kingr + 1, kingc - 1), (kingr + 1, kingc + 1)]
    for r, c in pawn_check_positions:
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'P':
            print("Success")
            return

    print("Fail")