from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # If A is a knight then he isn't a knave, and he can't be a knave and a knight.
    Biconditional(AKnight, Not(AKnave)),
    Not(And(AKnave, AKnight)),

    # If the sentence is true... A must be a knight
    Implication(And(AKnave, AKnight), AKnight),
    # But since the sentence can't be true... A must be knave
    Implication(Not(And(AKnave, AKnight)), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # If A/B is a knight then he isn't a knave, and he can't be a knave and a knight.
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),

    # If A is Knight then what he says must be true... and A/B are knaves
    Implication(And(AKnave, BKnave), AKnight),
    # If A is a Knave then what he says shouldn't be true... and A is a knaves and B is a Knight
    Implication(Not(And(AKnave, BKnave)), AKnave),
    # If A is Knight that B should be a Knave
    Implication(AKnight, BKnave),
    # If A is a Knave then B should be a Night
    Implication(AKnave, BKnight),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If A/B is a knight then he isn't a knave, and he can't be a knave and a knight.
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),

    # Giving both options of A, either what he said was true and he is a knight or he is a lair and knave
    Implication(And(AKnight, BKnight), AKnight),
    Implication(Not(And(AKnight, BKnight)), AKnave),
    # Giving both options for what B said, either that are different kinds and he is a knight or they are the same and he is a knave
    Implication(Or(And(AKnave, BKnight), And(AKnight, BKnave)), BKnight),
    Implication(Or(And(AKnave, BKnave), And(AKnight, BKnight)), BKnave),
    # If we know what A is, then we know what B has to be as well.
    Implication(AKnight, BKnight),
    Implication(AKnave, BKnight),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # If A/B/C is a knight then he isn't a knave, and he can't be a knave and a knight.
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(BKnave, BKnight)),
    # No matter what A is... by the rules of this game B is a knave
    Implication(AKnight, BKnave),
    Implication(AKnave, BKnave),
    # If B a is knave forsure then C must be a knight
    Implication(BKnave, CKnight),
    # if C is a knight A must be a knight
    Implication(CKnight, AKnight),
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
