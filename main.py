import sys
from stockfish import Stockfish
import argparse

parser = argparse.ArgumentParser("stockfish")
parser.add_argument("-f", metavar="--fen", help="fen string representing the current position", type=str)
parser.add_argument("-d", metavar="--depth", help="search depth stockfish should use", type=int)
parser.add_argument("-n", help="Find the top n moves", type=int)
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

fen = args.f
depth = args.d
n_moves = args.n

stockfish = Stockfish(path="/home/mauritz/Documents/stockfish-16/src/stockfish", depth=depth)

if stockfish.is_fen_valid(fen):
    stockfish.set_fen_position(fen)
else:
    print("Invalid fen")
    exit()


# get move in san (short algebraic notation) from lan (long algebraic notation)
def san(lan):
    san = ""
    start = lan[0:2]
    end = lan[2:4]

    piece = stockfish.get_what_is_on_square(start)
    if piece in (Stockfish.Piece.WHITE_QUEEN, Stockfish.Piece.BLACK_QUEEN):
        san = "Q" 
    if piece in (Stockfish.Piece.WHITE_KING, Stockfish.Piece.BLACK_KING):
        san = "K" 
    if piece in (Stockfish.Piece.WHITE_KNIGHT, Stockfish.Piece.BLACK_KNIGHT):
        san = "N" 
    if piece in (Stockfish.Piece.WHITE_BISHOP, Stockfish.Piece.BLACK_BISHOP):
        san = "B" 
    if piece in (Stockfish.Piece.WHITE_ROOK, Stockfish.Piece.BLACK_ROOK):
        san = "R" 

    if stockfish.will_move_be_a_capture(lan) in (Stockfish.Capture.DIRECT_CAPTURE, Stockfish.Capture.EN_PASSANT):
        san += "x"

    san += end
    return san

moves = stockfish.get_top_moves(n_moves)
print("Best moves")
for i in range(len(moves)):
    move = san(moves[i]["Move"])
    centipawn = moves[i]["Centipawn"] / 100
    if centipawn > 0:
        centipawn = f"+{centipawn}"

    print(f"{i+1}: {centipawn} {move}")
