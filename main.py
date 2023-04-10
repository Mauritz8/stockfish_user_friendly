from stockfish import Stockfish
import argparse

parser = argparse.ArgumentParser("stockfish")
parser.add_argument("-f", metavar="--fen", help="fen string representing the current position", type=str)
parser.add_argument("-d", metavar="--depth", help="search depth stockfish should use", type=int)
parser.add_argument("-n", help="Find the top n moves", type=int)
args = parser.parse_args()

fen = args.f
depth = args.d
n_moves = args.n

stockfish = Stockfish(path="/home/mauritz/Documents/code/stockfish_15/stockfish-ubuntu-20.04-x86-64", depth=depth)

if stockfish.is_fen_valid(fen):
    stockfish.set_fen_position(fen)
else:
    print("Invalid fen")
    exit()


moves = stockfish.get_top_moves(n_moves)
print("Best moves")
for i in range(len(moves)):
    move = moves[i]["Move"]
    centipawn = moves[i]["Centipawn"] / 100
    if centipawn > 0:
        centipawn = f"+{centipawn}"

    print(f"{i+1}: {centipawn} {move}")
