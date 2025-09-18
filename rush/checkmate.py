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

    drt = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in drt:
        r, c = kingr + dr, kingc + dc

        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]

            if piece != '.':
                straight = (dr == 0 or dc == 0)
                diagonal = (dr != 0 and dc != 0)

                if (straight and (piece == 'R' or piece == 'Q')) or \
                   (diagonal and (piece == 'B' or piece == 'Q')):
                    print("Success")
                    return

                break

            r = r + dr
            c = c + dc

    pawn_check = [(kingr + 1, kingc - 1), (kingr + 1, kingc + 1)]
    for r, c in pawn_check:
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'P':
            print("Success")
            return

    print("Fail")