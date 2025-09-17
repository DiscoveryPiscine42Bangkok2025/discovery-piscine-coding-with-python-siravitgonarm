from typing import List, Tuple, Union

def checkmate(*args) -> None:
    try:
        # --- Parse input into list of row-strings ---
        if len(args) == 0:
            return  # nothing to do
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, str) and '\n' in arg:
                rows = arg.splitlines()
            elif isinstance(arg, (list, tuple)):
                rows = list(arg)
            else:
                # single-row string without newline -> treat as 1x1 board
                rows = [str(arg)]
        else:
            # multiple args -> each arg is a row
            rows = [str(a) for a in args]

        n = len(rows)
        if n == 0:
            return

        # Convert to 2D board and validate square shape
        board: List[List[str]] = [list(r) for r in rows]
        for r in board:
            if len(r) != n:
                # not a square board -> undefined per spec, do nothing
                return

        # find the King's position
        king_pos: Union[Tuple[int,int], None] = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break
        if king_pos is None:
            # no king found -> undefined, do nothing
            return

        kr, kc = king_pos

        # --- Pawn check (pawn captures diagonally "ขึ้น" หนึ่งแถว) ---
        pawn_targets = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
        for r, c in pawn_targets:
            if 0 <= r < n and 0 <= c < n and board[r][c].upper() == 'P':
                print("Success")
                return

        # --- Sliding pieces: Rook (orthogonal), Bishop (diagonal), Queen (both) ---
        # Only the first piece on each ray can capture (others block)
        piece_set = {'Q', 'R', 'B', 'P', 'K'}  # pieces that can block/attack
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   # orthogonal (rook)
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonal (bishop)
        ]

        for dr, dc in directions:
            r, c = kr + dr, kc + dc
            while 0 <= r < n and 0 <= c < n:
                ch = board[r][c]
                ch_up = ch.upper()
                if ch_up not in piece_set:
                    # empty square (or irrelevant char) -> continue scanning
                    r += dr
                    c += dc
                    continue

                # found the first piece on this ray; decide if it attacks
                if dr == 0 or dc == 0:
                    # orthogonal ray -> rook or queen can attack
                    if ch_up in ('R', 'Q'):
                        print("Success")
                        return
                    else:
                        # blocked by non-attacking piece
                        break
                else:
                    # diagonal ray -> bishop or queen can attack
                    if ch_up in ('B', 'Q'):
                        print("Success")
                        return
                    else:
                        break

        # nothing found -> not in check
        print("Fail")
    except Exception:
        # any unexpected error -> silently return (per spec)
        return