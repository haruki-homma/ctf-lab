
import chess
import chess.pgn
from pathlib import Path

CIPHER = "nZ3ipU8_yy3p5_hvyKi0"
PGN = Path(__file__).with_name("Carlsen.pgn")

BOARD = [
    "AIWYAEIO",
    "JBKBFJPU",
    "XLCMKQVA",
    "ZCNDOWBE",
    "DGLPEQFI",
    "HMRXRFSK",
    "NSYCGTGU",
    "TZDHJLVH",
]


# チェス座標を文字に変換
def square_letter(square):
    row = 7 - chess.square_rank(square)
    col = chess.square_file(square)
    return BOARD[row][col]


# 復号
def decrypt(cipher, key):
    result = ""
    j = 0

    for c in cipher:
        if c.isascii() and c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            shift = ord(key[j % len(key)]) - ord("A")

            p = (ord(c) - base - shift) % 26
            result += chr(base + p)

            j += 1
        else:
            result += c

    return result


if not PGN.is_file():
    raise SystemExit(f"can't find the PGN file: {PGN}")

results = []

with PGN.open(errors="replace") as f:
    while (game := chess.pgn.read_game(f)) is not None:
        h = game.headers

        # 2026年の対局
        if not h.get("Date", "").startswith("2026"):
            continue

        white = h.get("White", "")
        black = h.get("Black", "")

        # Carlsenが白番
        if "Carlsen" not in white:
            continue

        # English Opening（A10～A39）
        eco = h.get("ECO", "")
        if not eco.startswith(("A1", "A2", "A3")):
            continue

        moves = list(game.mainline_moves())

        if not moves:
            continue

        # 初手が1.c4
        if moves[0].uci() != "c2c4":
            continue

        board = game.board()
        key = ""
        squares = []

        # Carlsen（白番）の指し手だけを抽出
        for move in moves:
            if board.turn == chess.WHITE:
                destination = move.to_square
                squares.append(chess.square_name(destination))
                key += square_letter(destination)

            board.push(move)

        if not key:
            continue

        plaintext = decrypt(CIPHER, key)

        results.append({
            "date": h.get("Date"),
            "black": black,
            "eco": eco,
            "key": key,
            "plaintext": plaintext,
        })


# 候補を表示
for i, r in enumerate(results, 1):
    print(f"\n===== MATCH {i} =====")
    print("Date:     ", r["date"])
    print("Black:    ", r["black"])
    print("ECO:      ", r["eco"])
    print("Key:      ", r["key"])
    print("Plaintext:", r["plaintext"])
