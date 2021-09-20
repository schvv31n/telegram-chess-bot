import collections
from typing import Optional

FENSYMBOLS = {
    "k": "King",
    "q": "Queen",
    "r": "Rook",
    "b": "Bishop",
    "n": "Knight",
    "p": "Pawn",
}
ENGINE_FILENAME = "./stockfish_14_x64"
STARTPOS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
BoardPoint = collections.namedtuple("BoardPoint", ("column", "row"), module="chess")


def decode_pos(pos: str) -> Optional[BoardPoint]:
    return BoardPoint(ord(pos[0]) - 97, int(pos[1]) - 1) if pos != "-" else None


def encode_pos(pos: BoardPoint) -> str:
    return chr(pos.column + 97) + str(pos.row + 1)


def in_bounds(pos: BoardPoint) -> bool:
    return 0 <= pos.column <= 7 and 0 <= pos.row <= 7


def is_lightsquare(pos: BoardPoint) -> bool:
    return pos.column % 2 != pos.row % 2
