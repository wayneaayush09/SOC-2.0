from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, And(AKnight, AKnave))
)


knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(AKnight, And(BKnave, AKnave))
)


knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave.
    Or(BKnight, BKnave),  # B is either a knight or a knave.
    Implication(AKnave, And(AKnave, BKnave)),
)

knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(BKnight, CKnave),
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnight, And(AKnight, AKnave)),
    Implication(BKnave, Not(And(AKnight, AKnave))),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()