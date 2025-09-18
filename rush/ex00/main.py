from checkmate import checkmate

def main():

    board1 = """\
K...
....
....
...."""
    checkmate(board1)

    board1 = """\
....
.K..
..P.
...."""
    checkmate(board1)

if __name__ == "__main__":
    main()